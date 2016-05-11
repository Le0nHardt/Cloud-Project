from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

class Relationship():
    def __init__(self, training_dict, training_label):
        self.training_dict = training_dict
        #self.test_dict = test_dict
        self.training_label = training_label
        self.clf = MultinomialNB()
        self.vectorizer = DictVectorizer()
        self.tfidf_transformer = TfidfTransformer()
    
    def train_data(self):
        
        
        training_data = self.vectorizer.fit_transform(self.training_dict)
        train_tfidf = self.tfidf_transformer.fit_transform(training_data)
        
        #clf = MultinomialNB()
        self.clf.fit(train_tfidf,self.training_label)
        
    def predict_data(self,test_dict):    
        test_data = self.vectorizer.transform(test_dict)
        test_tfidf = self.tfidf_transformer.transform(test_data)
        
        predictions = self.clf.predict(test_data)
        return predictions
        
        
        
        