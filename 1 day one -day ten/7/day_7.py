import twitter_credentials

from twitter import *


t = Twitter(auth=OAuth(twitter_credentials.access_token, 
	twitter_credentials.access_token_secret, 
	twitter_credentials.consumer_key, twitter_credentials.consumer_secret))

print(t.statuses.home_timeline())

t.direct_messages.events.new(
    _json={
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": t.users.show(screen_name="toktok911")["id"]},
                "message_data": {
                    "text": "henai !"}}}})
