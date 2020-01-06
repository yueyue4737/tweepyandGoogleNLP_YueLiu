# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the real-time tweets about a technology organization
# Reference1: Twitter Streaming API Documentation
# https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators
# Reference2: the source code
# https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py
# next step1: use the on_error method
# next step2: streaming api is different from REST api

import tweepy
import twitter_credentials

# StreamListener: classify the messages and route the method
# creating an object of the streamlistener
class MyStreamListener(tweepy.streaming.StreamListener):

    def __init__(self):
        pass

    def get_authentication(self):
        """get authentication"""
        # create an OAuthHandler instance
        auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
        # re-build the OAuthHandler from the stored access token
        auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
        return auth

    def get_stream(self, new_auth, new_listener, word_list):
        stream_tweets = tweepy.Stream(auth=new_auth, listener=new_listener)
        #stream_tweets.filter(track=word_list)
        stream_tweets.filter(track=word_list, is_async=True)
        return stream_tweets

    # def on_error(self, status_code):
    #     print(status_code)

if __name__ == '__main__':
    new_listener = MyStreamListener()
    new_auth = new_listener.get_authentication()
    word_list = ['kaggle']
    print(new_listener.get_stream(new_auth, new_listener, word_list))
