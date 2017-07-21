# Tweet Tweet

An example of how to use Python to create, read, and destroy Tweets.

## Prerequisites

Create a Twitter Account. Add your phone number to your Twitter Account, or else you won't be allowed to create a Twitter Application.

Then while logged in to Twitter, visit the [Twitter Application Management Console](https://apps.twitter.com/) and click "Create New App" to create a new Twitter Application.

After creating a new application, click on the "Keys and Access Tokens" tab, and note the application's "Consumer Key" and "Consumer Secret". Scroll down and generate a new Access Token and note its "Access Token" and "Access Token Secret" values. Store these four values in the following environment variables:

  + `TWITTER_API_KEY`
  + `TWITTER_API_SECRET`
  + `TWITTER_ACCESS_TOKEN`
  + `TWITTER_ACCESS_TOKEN_SECRET`

## Installation

Download the source code:

```shell
git clone git@github.com:s2t2/tweet-tweet-py.git
cd tweet-tweet-py/
```

Install package dependencies:

```shell
pip3 install -r requirements.txt
```

## Usage

This application is tested against Python 3.x and is not guaranteed to function with older versions.

```shell
python3 list_tweets.py
```

If you get an error message like: `tweepy.error.TweepError: [{'code': 89, 'message': 'Invalid or expired token.'}]`, ensure proper configuration of your environment variables.
