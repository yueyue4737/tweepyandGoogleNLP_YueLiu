# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# application mash
# Application Goal1: telling the twitter API(tweepy) to get the streaming tweets
# Application Goal2: asking the Google API(GOOGLE NLP) to analyze the sentiment
# next step1: file format conversion
# next step2: basic visualization(histogram)
# next step3: simple testing about the users' story
# next step4: use simple but correct terms

# import APIs and libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
import json
import os
import tweepy

# regenerate the twitter credentials when getting HTTP response code
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# getting the google credentials in the cloud platform
credentials_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'FILENAME.json'
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Program1: calling the APIs in the client library
class Client():
    def __init__(self):
        pass

    def twitter_authentication(self):
        """get the twitter authentication"""
        # create an OAuthHandler instance
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # re-build the OAuthHandler from the stored access token
        auth.set_access_token(access_token, access_token_secret)
        return auth

    def google_client(self):
        """setting up authentication in the cloud console"""
        client = language.LanguageServiceClient(credentials=credentials)
        return client

# Program2: getting the published tweets
class PublishedTweets():
    """
    get user timeline tweets
    """
    def __init__(self):
        pass

    def get_published_tweets(self, api, num):
        tweets = []
        # Cursor, about pages
        for tweet in tweepy.Cursor(api.user_timeline).items(num):
            tweets.append(tweet)
        return tweets

# Program3: getting the streaming tweets
class StreamingTweets(tweepy.streaming.StreamListener):
    """
    StreamListener: classify the messages and route the method;
    creating an object of the streamlistener
    """
    def __init__(self):
        pass

    def get_stream(self, new_auth, new_listener, word_list):
        stream_tweets = tweepy.Stream(auth=new_auth, listener=new_listener)
        stream_tweets.filter(track=word_list, is_async=True)
        return stream_tweets

# Program4: analyzing the sentiment of the tweets
class AnalyzingTweets():
    """Analyzing the tweets use Google NLP API"""
    def __init__(self):
        pass

    def sentiment_score(self, file_name):
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
        print('The sentiment score is', sentiment.score)

    def report_attitude(self, file_name):
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
    
    def print_hist(self):
        pass

# Program5: store the tweets in .json format
class StoreTweets():
    pass

if __name__ == 'main':
    """run only if the python file is not used as a module"""
    pass
