# Scraping hashtag on Twitter
# Author: @rodolfo-viana
# Requirement: Tweepy (http://www.tweepy.org/)

import codecs
import csv
import tweepy
from tweepy import OAuthHandler


class UTF8Recoder:

    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode('utf-8')

class UnicodeReader:

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, 'utf-8') for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode('utf-8') for s in row])
        data = self.queue.getvalue()
        data = data.decode('utf-8')
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

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
