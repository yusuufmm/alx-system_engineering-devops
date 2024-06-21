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

    try:
        results = response.json().get("data")
        after = results.get("after")  # Next page token
        children = results.get("children")
        
        for child in children:
            hot_list.append(child.get("data").get("title"))  # Collect titles

        if after is not None:
            return recurse(subreddit, hot_list, after)  # Recursive call for next page
        
        return hot_list  # Return list of titles when no more pages
    except Exception:
        return None  # Handle exceptions

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
