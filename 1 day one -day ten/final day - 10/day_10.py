import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)