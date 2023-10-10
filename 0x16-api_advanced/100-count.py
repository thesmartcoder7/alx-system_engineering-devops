#!/usr/bin/python3
"""
this a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()

    if not word_list:
        for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word.lower()}: {count}")
        return

    if subreddit is None:
        return

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

            titles = [post["data"]["title"].lower() for post in posts]

            for word in word_list:
                counts[word] += titles.count(word.lower())

            after = data["data"]["after"]
            if after:
                return count_words(subreddit, word_list, after, counts)
        except KeyError:
            return None
