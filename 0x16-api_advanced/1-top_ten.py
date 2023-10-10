#!/usr/bin/python3
"""
this Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """this prints the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    req = requests.get(
        f'http://www.reddit.com/r/{subreddit}/hot.json',
        headers={'User-Agent': 'Python/requests:APIproject:\
        v1.0.0 (by /u/aaorrico23)'}, params={'limit': 10}
    ).json()
    posts = req.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
