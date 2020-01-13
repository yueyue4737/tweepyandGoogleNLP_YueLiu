# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the public tweets from a famous organization user
# @kaggle
# Help understand the numeric id
# Help understand the number limits

import twitter_credentials
import twitter
#import python_twitter --> this is the wrong name

def get_authentication():
    api = twitter.Api(consumer_key=twitter_credentials.consumer_key,
                      consumer_secret=twitter_credentials.consumer_secret,
                      access_token_key=twitter_credentials.access_token,
                      access_token_secret=twitter_credentials.access_token_secret)
    return api

def get_public_tweets(api,screen_name):
    '''get published tweets from a specific user'''
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    return timeline

def get_retweeters(status_id):
    '''returns a list of users ID up to 100'''
    retweeters = api.GetRetweeters(status_id)
    return retweeters

# if __name__ == 'main': --> don't use it without classes/main function
api = get_authentication()
screen_name = 'kaggle'
public_tweets = get_public_tweets(api, screen_name)
print(public_tweets)
status_id = '1215664689662824450'
print(get_retweeters(status_id))
