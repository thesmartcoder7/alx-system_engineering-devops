#!/usr/bin/python3
"""
Contains the recurse function
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of all hot post titles for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    req = requests.get(
        f'http://www.reddit.com/r/{subreddit}/hot.json',
        headers={'User-Agent': 'Python/requests:APIproject:\
        v1.0.0 (by /u/aaorrico23)'}, params={'after': after}
    ).json()

    after = req.get('data', {}).get('after', None)
    posts = req.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
