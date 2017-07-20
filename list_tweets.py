import tweepy

#
# Use Environment Variables to access passwords while keeping them private
#

consumer_key = _________
consumer_secret = _________

#
# Boilerplate code from http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html ...
#

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet.text
