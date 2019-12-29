# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the real-time tweets about a competition
# Reference1: Twitter Streaming API Documentation
# https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators
# Reference2: the source code
# https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py
# @kaggle
# summary: streaming api is different from REST api
# next step1: change a container for the user relationships

import tweepy
import twitter_credentials

# StreamListener: classify the messages and route the method
# inheritaing from streamlistener
class MyStreamListener(tweepy.StreamListener):
    # use OAuth 1a for application user only
    def get_authentication():
        """get authentication"""
        # create an OAuthHandler instance
        auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
        # re-build the OAuthHandler from the stored access token
        auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
        api = tweepy.API(auth)
        return api

    def get_stream(self, status, word):
        print(status.text)
        newStreamListener = MyStreamListener()
        stream_tweets = tweepy.Stream(auth=self.get_authentication(), listener=newStreamListener)
        stream_tweets.filter(track=[str(word)], is_async=True)
        return stream_tweets

if __name__ == 'main':
    pass
