# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# an individual application mash
# Application Goal1: telling the twitter API(tweepy) to get the streaming tweets
# Application Goal2: asking the Google API(auto NLP) to analyze the sentiment

# import libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
import numpy as np
import os
import pandas as pd
import tweepy

# credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
credentials_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "[FILENAME].json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# authentication
# create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# re-build the OAuthHandler from the stored access token
auth.set_access_token(access_token, access_token_secret)
client = language.LanguageServiceClient(credentials=credentials)

# Program1: getting the public tweets
def get_public_tweets(api,user,n):
    """get public tweets"""
    public_tweets = []
    # blocked when using home_timeline
    # user_timeline can help us get the specified tweets
    target = tweepy.Cursor(api.user_timeline, id=user)
    for tweet in target.items(n):
        public_tweets.append(tweet)
    return public_tweets

def get_relationship(api,user):
    """get retweeters, friends lists and followers"""
    friends_list = []
    friends = api.friends(id=user)
    for i in friends:
        friends_list.append(i)
    followers_list = []
    followers = api.followers(id=user)
    for j in followers:
        followers_list.append(j)
    return friends_list, followers_list

def get_retweets(self, id):
    """require the numeric id"""
    retweets = self.api.retweet(id)
    return retweets

# Program2: getting the real-time tweets
class StdOutListener(tweepy.StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        with open("streaming.json", 'w') as f:
            f.write(data)
        return True

    def on_error(self, status):
        print(status)

# Program3: analyzing the sentiment of the tweets
def sentiment_analysis(file_name):
    """
    Sentiment Analysis by using Google Natural Language API
    :param file_name:
    :return: string-reaction
    """
    # fetch the file for analysis
    # sentiment analysis by the basic methods
    with open(file_name, 'r') as file:
        content = file.read()
    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    # measure the tweets by using score and magnitude
    score = sentiment.score
    magnitude = sentiment.magnitude
    reaction = 'Neutral'
    if score > 0.3:
        reaction = 'Positive'
    elif score <= -0.3:
        reaction = 'Negative'
    else:
        if magnitude > 3:
            reaction = 'Mixed'
    return reaction

if __name__ == '__main__':
    print("Hit control-z when you want to terminate the streaming!")
    api = tweepy.API(auth)
    user = 'NationalVOAD'
    tweets = get_public_tweets(api,user,200)
    label_df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
    label_df['id'] = np.array([tweet.id for tweet in tweets])
    label_df['keyword'] = np.array([tweet.id for tweet in tweets])
    label_df['location'] = np.array([tweet.id for tweet in tweets])
    label_df['text'] = np.array([tweet.id for tweet in tweets])
    label_df['target'] = np.array([tweet.id for tweet in tweets])
    sentiment_tweets = get_public_tweets(api, user, 1)
    with open("sentiment_tweets.txt", "w") as f:
        for tweet in tweets:
            f.write(tweet.text)
        f.close()
    print(sentiment_analysis("sentiment_tweets.txt"))
    label_df.to_csv('label.csv')
    my_listener = StdOutListener()
    stream = tweepy.Stream(auth, my_listener)
    stream.filter(track=['disaster'])
