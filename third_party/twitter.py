import os
from datetime import datetime, timezone
import logging

import tweepy
import requests

logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)
auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)


def scrape_user_tweets(username, num_tweets=20):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """

    # error occurred because tweets api policy is changed
    # tweets = api.user_timeline(screen_name=username, count=num_tweets)
    # use gist
    tweet_list = requests.get(
        "https://gist.githubusercontent.com/sonagihu/4256a3b5e6ab32012ae8f3fc82141290/raw/89da058be009b85f78919e541a3d39b5a615dee1/gistfile1.txt"
    )

    # tweet_list = []

    # for tweet in tweets:
    #     if "RT @" not in tweet.text and not tweet.text.startswith("@"):
    #         tweet_dict = {}
    #         tweet_dict["time_posted"] = str(
    #             datetime.now(timezone.utc) - tweet.created_at
    #         )
    #         tweet_dict["text"] = tweet.text
    #         tweet_dict[
    #             "url"
    #         ] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
    #         tweet_list.append(tweet_dict)

    return tweet_list.json()