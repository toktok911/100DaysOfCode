import twitter_credentials

from twitter import *


t = Twitter(auth=OAuth(twitter_credentials.access_token, 
	twitter_credentials.access_token_secret, 
	twitter_credentials.consumer_key, twitter_credentials.consumer_secret))


x = t.search.tweets(q="Sudan", count=1) 
print(dir(x))
