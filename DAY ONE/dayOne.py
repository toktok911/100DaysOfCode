# streaming the tweets directly from twitter in realtime. 
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream 

import twitter_credentials

#we want to create a clasa which will allow us to print the tweets. 
#we call it stdoutListener, and it is going to inherit from StreamListener
#stdoutListener has some methods that we want to override.

class MyStreamListener(StreamListener): 
	
	def on_data(self, data): 
		print(data)
		return True
	
	def on_error(self,status):
		print(status)

if __name__=="__main__":
	listener = MyStreamListener()
	auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
	auth.set_access_token(twitter_credentials.access_token,twitter_credentials.access_token_secret)
	
	stream = Stream(auth, listener)

	stream.filter(track=['sudan revolts','sudan uprising','تسقط بس'])
