# -*- coding: utf-8 -*-
'''
    Reference:
        Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social
        Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import proprecessing
import json

class Sentiment_Analysis():
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()
        word_list = set(nltk.corpus.words.words())
        wordnet_lemmatizer = WordNetLemmatizer()
        self.preprocess = proprecessing.Preprocess(word_list, wordnet_lemmatizer)
        self.stop_words = set(stopwords.words('english'))
        self.punctuatoins = set(string.punctuation)
        self.file_emoji = open('emoji_set.json','r')
        self.jsons = json.load(self.file_emoji)

    def sentiment_analysis(self, tweet_content, hashtags, hashtags_irrelevant):
        tweet_content += ' '
        tweet_content = self.preprocess.remove_username(tweet_content)
        tweet_content = self.preprocess.remove_URL(tweet_content)
        
        # is_target is True means that the tweet is relevant with our topic
        # is_irrelevant is True means that the tweet is irrelevant with our topic.
        tweet_sentiment, is_target, is_irrelevant = self.preprocess.handle_hashtag(tweet_content,hashtags,hashtags_irrelevant)
        tweet_sentiment = tweet_sentiment.encode('unicode_escape')
        score = self.sid.polarity_scores(tweet_sentiment)
        positive = score['pos']
        negative = score['neg']
        neutral = score['neu']
        
        # For training data, we do not split hashtag contents, so just simply remove the '#'
        tweet_content = self.preprocess.hand_hashtag_for_relationship(tweet_content)
        # Since the third-party module may be sensitive capital letter, the lower() method
        # does not call before building bag of words.
        tweet_content = tweet_content.lower()
        tweet_words = self.preprocess.segment_tokenize(tweet_content)
        tweet_words = filter(lambda w: True if w not in self.stop_words else False, tweet_words)
        tweet_words = filter(lambda w: True if w not in self.punctuatoins else False, tweet_words)
        
        BOW = self.preprocess.build_BOW(tweet_words)
        
        if positive > negative and positive > neutral:
            return 1, BOW, is_target, is_irrelevant
        if negative > positive and negative > neutral:
            return -1, BOW, is_target, is_irrelevant
        if neutral > negative and neutral > positive:
            return 0, BOW, is_target, is_irrelevant
        return 0, BOW, is_target, is_irrelevant
    
    def handle_emoji(self,tweet):
        for key in self.jsons.keys():
            if key in tweet:
                tweet = tweet.replace(key,' '+self.jsons[key]+' '+self.jsons[key]+' ')
        return tweet        
        
