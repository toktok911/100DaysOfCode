# streaming the tweets directly from twitter in realtime. 
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 

import twitter_credentials

#we want to create a clasa which will allow us to print the tweets. 
#we call it stdoutListener, and it is going to inherit from StreamListener
#stdoutListener has some methods that we want to override.
class TwitterStreamer():
	"""
	This class handles twitter authentication and connection to the API
	"""
	def stream_tweets(self, tweets_filename, hashtags_list):
		listener = MyStreamListener()
		auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
		auth.set_access_token(twitter_credentials.access_token,twitter_credentials.access_token_secret)
		
		stream = Stream(auth, listener)
		stream.filter(track=hashtags_list)


class MyStreamListener(StreamListener): 
	def __int__(self, tweets_filename):
		self.tweets_filename = tweets_filename

	
	
	def on_error(self,status):
		print(status)

if __name__=="__main__":
	hashtags_list = ["#تسقط_بس", "#مدن_السودان_تنتفض"]
	tweets_filename = "tweets.txt"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(tweets_filename, hashtags_list)