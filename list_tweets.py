import os
import tweepy
from IPython import embed

#
# Use Environment Variables to access passwords while keeping them private
#    reference: https://github.com/prof-rossetti/nyu-info-2335-70-201706/blob/master/notes/programming-languages/python/modules/os.md
#

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

#
# Boilerplate code from http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html ...
#

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#
# API Usage
#

user = api.me()
print("---------------------------------------------------------------")
print("RECENT TWEETS BY @{0} ({1} FOLLOWERS / {2} FOLLOWING):".format(user.screen_name, user.followers_count, user.friends_count))
print("---------------------------------------------------------------")

tweets = api.user_timeline() # why are deleted tweets showing up in here? contacted twitter support...

for tweet in tweets:
    created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M")
    print(" + ", created_at, "|", tweet.text)
