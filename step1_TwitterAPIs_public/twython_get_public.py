# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the public tweets from a famous organization user
# @kaggle
# Help understand Error condition

import twitter_credentials
import twython

def get_authentication():
    api = twython.Twython(twitter_credentials.consumer_key,
                          twitter_credentials.consumer_secret,
                          twitter_credentials.access_token,
                          twitter_credentials.access_token_secret)
    return api

def get_public_tweets(api,screen_name):
    try:
        user_timeline = api.get_user_timeline(screen_name=screen_name)
    except twython.TwythonError as e:
        print(e)
    print(user_timeline)

api = get_authentication()
screen_name = 'kaggle'
public_tweets = get_public_tweets(api, screen_name)
print(public_tweets)
