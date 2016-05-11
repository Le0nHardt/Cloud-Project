import couchdb
import json

class Handle_DB():
    def __init__(self,url):
        self.server = couchdb.Server(url)
        try:
            self.db = self.server.create('tweets')
        except:
            self.db = self.server['tweets']
    
    def add_tweet(self, id, tweet, BOW, sentiment, city, label):
        #print ('add doc')
        try:
            self.db[json.dumps(id)] = {'tweet':tweet,'BOW':json.dumps(BOW),'sentiment':sentiment,'city':city,'label':label}

        except couchdb.http.ResourceConflict:
            pass        
            #print ('couchdb.http.ResourceConflict')  
     
    def querySentiment(self,key):
        #for sentiment, the key should be -1 or 0 or 1
        map_func = '''function(doc){
                    emit(doc.sentiment,1);
                    }'''

        reduce_func = '_count'
        
        result = self.db.query(map_func,reduce_func)
        count = result[key:key]
        for row in count:    
            value = row.value
        return value
    
    def query_class(self,key):
        map_func = '''function(doc){
                    emit(doc.label,1);
                    }'''

        reduce_func = '_count'
        
        result = self.db.query(map_func,reduce_func)
        count = result[key:key]
        for row in count:    
            value = row.value
        return value
    
    def total_length(self):
        return len(self.db)
    
    def update_label(self,doc_id,label):        
        doc = self.db[doc_id]
        doc['label'] = label
        self.db.save(doc)
    
    def get_db(self):
       return self.db    