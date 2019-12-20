# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: use tweepy to get public data
# miniproject 1: get the public data with fewer lines
# miniproject 3: get the correct file format for DB

import json
import numpy as np
import pandas as pd
# http://docs.tweepy.org/en/latest/index.html
import tweepy

# import twitter_credential -> if we are handling a large program
# register twitter client application(need a personal twitter account)
# get 4 strings here: https://developer.twitter.com/en/apps
# do not change the sequence
# do not leak to others
KEY = ''
KEY_SECRET = ''
TOKEN = '' # this is a key
TOKEN_SECRET = '' # this is a secret

# http://docs.tweepy.org/en/latest/auth_tutorial.html
def authorize():
    """authorize twitter, initialize tweepy:
     OAuth 1a (application-user) """
    auth = tweepy.OAuthHandler(KEY, KEY_SECRET)
    auth.set_access_token(TOKEN, TOKEN_SECRET)
    return auth

# http://docs.tweepy.org/en/latest/cursor_tutorial.html
def get_public_tweets(num):
    """get user timeline tweets:
    Cursor, about pages"""
    api = tweepy.API(authorize())
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline).items(num):
        tweets.append(tweet)
    return tweets

def print_data_frame(tweets):
    """structured data"""
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])
    df['id'] = np.array([tweet.id for tweet in tweets])
    df['len'] = np.array([len(tweet.text) for tweet in tweets])
    df['date'] = np.array([tweet.created_at for tweet in tweets])
    df['source'] = np.array([tweet.source for tweet in tweets])
    df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
    df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    return df

if __name__ == '__main__':
    api = tweepy.API(authorize())
    # http://docs.tweepy.org/en/latest/api.html#API.user_timeline
    # by default, we use the first 20
    tweets = api.user_timeline(screen_name="voguemagazine", count=100) # make sure to use the correct name
    df = print_data_frame(tweets)
    for i in range(10):
        print("The number of retweet for line", i, "is", tweets[i].retweet_count)
    print(df.head(100))
# .csv: a comma-separated values file, open in Microsoft Excel or R
    df.to_csv("tweet.csv")
# .json: JavaScript Object Notation, open in data base
    with open('tweet.json', 'w') as f:
        for tweet in tweets:
            json.dump(tweet._json, f, sort_keys=True, indent=4)
        f.close() # an important step for safety issue
