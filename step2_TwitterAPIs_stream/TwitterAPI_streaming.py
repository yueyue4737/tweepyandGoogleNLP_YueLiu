# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the real-time tweets about a technology organization
# @kaggle
# Help understand the HTTP Request
# Help understand the necessary to know the running time

import TwitterAPI
import twitter_credentials

def get_authentication():
    api = TwitterAPI.TwitterAPI(twitter_credentials.consumer_key,
                     twitter_credentials.consumer_secret,
                     twitter_credentials.access_token,
                     twitter_credentials.access_token_secret)
    return api

def streaming_tweets(api,track_term):
    result = api.request('statuses/filter', {'track':track_term})
    for i in result:
        print(i['text'] if 'text' in i else i)

api = get_authentication()
track_term = 'kaggle'
streaming = streaming_tweets(api,track_term)
