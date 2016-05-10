import tweepy
import json
import time
import codecs
consumer_key = 'RdvHXkPFLL0cu8QvI3PdoQ'
consumer_secret = 'mo5kWMvbX6aug5CVLWgCunmHDXMFlp7Ui08S4tig4'
access_token = '126863731-edOdSBsOCL6CVJmvHx5MrK6vxFBaOL0AL1Le6jrT'
access_token_secret = 'dEguctzXUTeRLZ9GTRkhIPRFiQBEKqI4618lbo9tHHmLq'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

file = codecs.open('./tweets.json','a','utf-8')
since = 0
flag = 0
while True:
    try:
        for status in tweepy.Cursor(api.search,lang='en',since_id = since,rpp = 100,geocode = '-37.8142509460,144.9631652832,20km').items(1500):
            since = status.id
            json_status = json.dumps(status._json)
            file.write(json_status+'\n')
    except:
        time.sleep(15 * 61)


