# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: get the public tweets from a famous organization user
# @kaggle
# next step1: get a standard authentication method, api might not be a better return variable
# next step2: (choose specific variable and) store the list of data in a file/database

import tweepy
import twitter_credentials

# use OAuth 1a for application user only
def get_authtication():
    """get authentication"""
    # create an OAuthHandler instance
    auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    # re-build the OAuthHandler from the stored access token
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    api = tweepy.API(auth)
    return api

# as an editor for a technology organization/magazine,
# I will start from the published twitters
def get_public_tweets(api,user,n):
    """get public tweets"""
    public_tweets = []
    # blocked when using home_timeline
    # user_timeline can help us get the specified tweets
    target = tweepy.Cursor(api.user_timeline, id=user)
    for tweet in target.items(n):
        public_tweets.append(tweet)
    return public_tweets

# the following 3 methods are to help analyze
# def get_retweeters(api):
#     """get retweets"""
#     return api.retweeters(id=80422885)

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

if __name__ == '__main__':
    api = get_authtication()
    user = 'kaggle'
    print(get_public_tweets(api,user,10))
    #print(get_retweeters(api))
    print(get_relationship(api,user))
