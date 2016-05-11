import json
import sys
import sentiment_analysis
import relationship
import setting
import handle_db
import couchdb

# Setting the path of the data file.
file_path = '/mnt/test/tweets.json'

server_URL = 'http://118.138.247.75:5984/'
db = handle_db.Handle_DB(server_URL)

city = ''
args = []
is_add_data = False
is_query_data = False
is_train_data = False
try:
    if len(sys.argv) > 1:
        for i in range(1,len(sys.argv)):
            args.append(sys.argv[i])
        if 'add_data' in args:
            is_add_data = True
            city = args[args.index('add_data') + 1]
        elif 'query_data' in args:
            is_query_data = True
        elif 'train_data' in args:
            is_train_data = True
        else:
            print 'Please input correct parameters'
            exit()
except:
    print 'Please input correct parameters'
    exit()


# The hash hashtag should be lower case.
# Put relevant topics in the hashtag, put irrelevant topics in the hashtag_irrelevant
hashtag = ['#auspol']
hashtag_irrelevant = ['#brisbane','#asmsg','#ian1','#qld','#travel','#nowplaying','#sydney','#adelaide', '#melbourne','#adlvmcy','#weflyasone','#alfinals','#quote']

# To make sure, tweet ID is unquie.
tweet_ids = set()

target_dict = []
target_class = []
target_id = []
target_sentiment = [] 

irrelevant_dict = []
irrelevant_class = []
irrelevant_id = []
irrelevant_sentiment = [] 

unsure_dict = []
unsure_class = []
unsure_id = []
unsure_sentiment = [] 

training_dict = []
training_class = []
training_id = []
training_sentiment = []

test_dict = []
test_class= []
test_id = []
test_sentiment = []

sent_analysis = sentiment_analysis.Sentiment_Analysis()


def preprcess_add_data():
    with open(file_path, 'r') as f:
        for line in f:
            try:
                tweet_json = json.loads(line)
                tweet_content = tweet_json['text']
                twwet_id = tweet_json['id']
                if twwet_id not in tweet_ids:
                    sentiment,BOW, is_target,is_irrelevant = sent_analysis.sentiment_analysis(tweet_content,hashtag,hashtag_irrelevant)
                    #print twwet_id,tweet_content, sentiment
                    label = -1
                    tweet_ids.add(twwet_id)
                    if is_target:
                        label = 1
                        target_dict.append(BOW)
                        target_class.append(label)
                        target_id.append(twwet_id)
                        target_sentiment.append(sentiment)
                    elif is_irrelevant:
                        label = 0
                        irrelevant_dict.append(BOW)
                        irrelevant_class.append(label)
                        irrelevant_id.append(twwet_id)
                        irrelevant_sentiment.append(sentiment)
                    else:
                        unsure_dict.append(BOW)
                        unsure_class.append(label)
                        unsure_id.append(twwet_id)
                        unsure_sentiment.append(sentiment)
            except:
                print 'error'
            db.add_tweet(twwet_id,tweet_content,BOW,sentiment,city,label)
            
def query_sentiment():
    positive = 0
    negative = 0
    neutral = 0
    positive = db.querySentiment(1)
    negative = db.querySentiment(-1)
    neutral = db.querySentiment(0)
    dic = {'positive':positive,'neutral':neutral,'negative':negative}
    return dic
    
def query_class():
    relevant = db.query_class(1)
    irrelevant = db.query_class(0)
    unsure = db.query_class(-1)
    dic = {'relevant':relevant,'irrelevant':irrelevant,'unsure':unsure}
    return dic
    
if is_add_data:
    preprcess_add_data()
if is_query_data:
    print query_sentiment()
    print query_class()
    print db.total_length()

if is_train_data:
    f = open('log.txt','w')
    f.write('start\n')
    f.flush()     
    url_list = ['http://118.138.247.76:5984/','http://118.138.247.81:5984/','http://118.138.247.63:5984/','http://118.138.247.75:5984/']
    server_list = []
    # get all training data
    for i in range(len(url_list)):
        f.write('process ' + str(url_list[i])+'\n')
        f.flush()        
        database = couchdb.Server(url_list[i])['tweets']          
        
        rows = database.view('_all_docs', limit= 760000,include_docs=True)
        docs = [row.doc for row in rows]
        for d in docs:
            try:                         
                label = d['label']                                  
                BOW = json.loads(d['BOW'])                
                if label == 1 or label == 0:                
                    training_dict.append(BOW)
                    training_class.append(label)
                elif url_list[i] == server_URL and label == -1:
                    # only store local test data
                    test_dict.append(BOW)
                    test_id.append(d.id)
            except:
                pass
        f.write(str(url_list[i]) + ' finish\n')
        f.flush()
    
    relation = relationship.Relationship(training_dict,training_class)
    relation.train_data()
    f.write('training finish\n')
    f.flush()      
        
    f.write ('start predicting\n')
    f.flush()        
    predictions = relation.predict_data(test_dict)    
    f.write ('predict finish\n')
    f.flush()
 
    f.write ('start update\n')
    f.flush()
             
    for j in range(len(predictions)):
        test_docs[j]['label'] = predictions[j] 
    
    f.write ('save in file\n')
    f.flush()    
    dat = open('predict_docs','w')
    dat.write(json.dumps(docs))
    dat.flush()
    dat.close()
      
                   
    f.write ('writing to DB\n')
    f.flush()
    DB = couchdb.Server(server_URL)['predict']
    l = len(test_docs)
    finish = False
    m = 0
    n = 100000
    while(not finish):
        if n<l:                  
            doc = test_docs[m:n]
            DB.update(doc)
            m = n
            n = m + 100000              
        elif n>=l:
            n = l            
            doc = test_docs[m:n]
            DB.update(doc)
            finish = True  
     
    f.write ('update finished\n')
    f.flush()             
    f.close()
            
            
