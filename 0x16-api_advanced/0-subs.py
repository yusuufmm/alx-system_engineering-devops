#!/usr/bin/python3
"""
Module to query the number of subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        return 0
    except requests.RequestException:
        return 0
