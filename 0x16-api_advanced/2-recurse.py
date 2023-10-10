#!/usr/bin/python3
"""
this is a recursive function that queries the Reddit API
and returns a list of titles of all hot articles for a
given subreddit. 
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if not hot_list:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "YourFriendlyNeighbourhood/1.0 (by YourFriendly)"
    }

    if after:
        url += f"&after={after}"

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data["data"]["children"]

            for post in posts:
                hot_list.append(post["data"]["title"])

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except KeyError:
            return None
    else:
        return None
