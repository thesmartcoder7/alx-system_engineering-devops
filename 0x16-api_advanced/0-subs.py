#!/usr/bin/python3
"""
this Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    res = requests.get(
        f'http://www.reddit.com/r/{subreddit}/about.json',
        headers={'User-Agent': 'Python/requests:APIproject:\
        v1.0.0 (by /u/aaorrico23)'}
    ).json()
    subs = res.get("data", {}).get("subscribers", 0)
    return subs
