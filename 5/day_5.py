# streaming the tweets directly from twitter in realtime. 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

import twitter_credentials

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth=TwitterAuthenticator().authenticate_twitter()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
    
    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_tweets(self, num_tweets):
        tweets = []
        for t in Cursor(self.twitter_client.user_timeline, id= self.twitter_user).items(num_tweets):
            tweets.append(t)
        return tweets

#we want to create a clasa which will allow us to print the tweets. 
#we call it stdoutListener, and it is going to inherit from StreamListener
#stdoutListener has some methods that we want to override.
class TwitterAuthenticator():
    def  authenticate_twitter(self):
        auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
        auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)   
        return auth

class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()##

    def stream_tweets(self, tweets_filename, hashtags_list):
        listener = MyListener(tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter()##
        stream = Stream(auth, listener)
        stream.filter(track=hashtags_list)


class MyListener(StreamListener):

    def __init__(self, tweets_filename):
        self.tweets_filename = tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        if status ==420:
            return False
        print(status)

class TweetAnalyzer():
    def tweets_to_dataframe(self, tweets):
        df = pd.DataFrame(data=[t.text for t in tweets], columns=['Tweets'])

        df['id'] = np.array([t.id for t in tweets])
        df['len'] = np.array([len(t.text) for t in tweets])
        df['date'] = np.array([t.created_at for t in tweets])
        df['source'] = np.array([t.source for t in tweets])
        df['likes'] = np.array([t.favorite_count for t in tweets])
        df['retweets'] = np.array([t.retweet_count for t in tweets])

        return df

if __name__ == '__main__':
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screen_name="toktok911", count="20" )
    tweet_analyzer=TweetAnalyzer()###
    df = tweet_analyzer.tweets_to_dataframe(tweets)#

    #print(np.mean(df['len']))
    #print(np.max(df['likes']))
    time_retweet = pd.Series(data=df['retweets'].values, index=df['date'])
    time_retweet.plot(figsize=(16, 4), label='retweet', legend=True)

    time_likes = pd.Series(data=df['likes'].values, index=df['date'])
    time_likes.plot(figsize=(16, 4), label='likes', legend=True)
    
    plt.show()