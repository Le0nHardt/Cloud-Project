'''
    This purpose of this class is to pre-process data, which contains remove URL,
    remove username, and handle hashtag of tweets.
'''
import re
import nltk
import nltk.data
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize
from nltk.stem import *


class Preprocess():    
    def __init__(self,word_list_set,wordnet_lemmatizer):
        self.word_list = word_list_set
        self.wordnet_lemmatizer = wordnet_lemmatizer
        self.stemmer = PorterStemmer()
    
    def remove_URL(self, tweet):
        re_url = r'http.+?\s'
        return re.sub(re_url, ' ', tweet) 
    
    
    def max_match(self, sentence, words):
        if len(sentence) == 0:
            return
        for i in range(len(sentence), 0, -1):
            firstword = sentence[0:i]
            remainder = sentence[i:len(sentence)]
            if self.wordnet_lemmatizer.lemmatize(firstword.lower()) in self.word_list \
                or self.wordnet_lemmatizer.lemmatize(firstword.lower(),pos='v') in self.word_list:
                words.append(firstword)
                self.max_match(remainder, words)
                return
        firstword = sentence[0:1]
        remainder = sentence[1:len(sentence)]
        words.append(firstword)
        self.max_match(remainder, words)
        return
    
    def remove_username(self, tweet):
        re_username = r'@.+?\s'
        return re.sub(re_username,' ', tweet)
    
    # Remove hash tages and replace these hash tags to their content(one or serveral words).
    # the parameter 'title' should be a list, which contains the particular hashtags.
    def handle_hashtag(self, tweet, titles, non_titles):
        re_hashtag = r'#.*?\s'
        # Find out all hash tags of a tweet
        tags = re.findall(re_hashtag, tweet)
        is_target = False      
        is_irrelevant = False  
        for tag in tags:
            result = []
            tag_lower = tag.lower().strip()
    
            if tag_lower in titles:
                is_target = True
            if tag_lower in non_titles:
                is_irrelevant = True
            
            self.max_match(tag_lower.replace('#',''),result)
            str_replace = ""
            # Convert list of words (splited by maxMatch Algorithm) to a sentences or a phrase
            for r in result:
                str_replace += r + " "
            tweet = tweet.replace(tag, str_replace)  
        #print tags
        return tweet, is_target, is_irrelevant
    
    # Replace all '#' to ''
    def hand_hashtag_for_relationship(self, tweet):
        tweet = tweet.replace('#','')
        return tweet
    
    # Segment tweets into sentences, and tokenize them
    def segment_tokenize(self, tweet):
        token = wordpunct_tokenize(tweet)
        return token
    
    def build_BOW(self, word_list):
        BOW = {}
        for word in word_list:
            word = self.stemmer.stem(word)
            BOW[word] = BOW.get(word, 0) + 1
        return BOW 
    
    

    
        
    