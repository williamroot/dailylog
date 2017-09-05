# Scraping hashtag on Twitter
# Author: @rodolfo-viana
# Requirement: Tweepy (http://www.tweepy.org/)

import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

max_tweets = 999999999

with open('tweets.csv', 'w', encoding='utf-8') as f:
    for tweet in tweepy.Cursor(api.search, q='whateverhashtagyouwant', rpp=100).items(max_tweets):
        print(tweet.created_at, tweet.text)
        wr = csv.writer(f, delimiter=';', lineterminator='\n')
        wr.writerow([tweet.created_at, tweet.text])