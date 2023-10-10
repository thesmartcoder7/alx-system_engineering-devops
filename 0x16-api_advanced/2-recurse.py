#!/usr/bin/python3
"""
this is a recursive function that queries the Reddit API
and returns a list of titles of all hot articles for a
given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    user_agent = 'Linux:Ubuntu/google'
    headers = {
        'User-Agent': user_agent
    }
    params = {
        'limit': 100,
        'after': after
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if res.status_code != 200:
        return None

    data = res.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after=after)
    else:
        return hot_list
