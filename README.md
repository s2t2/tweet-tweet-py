# Tweet Tweet

An example of how to use Python to create, read, and destroy Tweets.

## Prerequisites

Create a Twitter account and send a few example Tweets from it. Or use your own Twitter account, but be careful.

Then while logged in to Twitter, visit the [Twitter Application Management Console](https://apps.twitter.com/) and click "Create New App"

After creating a new application, note its "Consumer Key" and "Consumer Secret". These are secret passwords that should not be shared or tracked in version control. Store your application's passwords in environment variables called something like `TWITTER_API_KEY` and `TWITTER_API_SECRET`, respectively.

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
