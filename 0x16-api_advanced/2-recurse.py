#!/usr/bin/python3
""" recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns list of titles of all hot posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None  # Subreddit not found

    results = response.json().get("data")
    after = results.get("after")  # Next page token
    count += results.get("dist")  # Update count
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))  # Collect titles

    if after is not None:
        return recurse(subreddit, hot_list, after, count)  # Recursive call for next page
    return hot_list  # Return list of titles
