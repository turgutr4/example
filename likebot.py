import tweepy
import time
import random
import os
from userids import hashtags


# Authenticate to Twitter
auth = tweepy.OAuthHandler("WemSltdC8OjSVp596sUPMJ2LK",
                           "oZczVKHJrbpjK8gMLQibd95ZQQODTF1P7ARj42RZK6gf9RRijI")
auth.set_access_token("956507305960509440-DjE9qtb08LD8n7AqfWfFsGyPqr6WwXI",
                      "7PX7hqOaXOalgS8ISdy7CSCwaWf2yOWMQBLfkJkBYmAN2")


api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


for tweet in tweepy.Cursor(api.search, q=random.choice(hashtags)).items(10):
    try:
        tweet.favorite()
    except StopIteration:
        break
