#!/usr/bin/python3
"""define the function recurse"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, params=params, headers={
        'User-Agent': 'My User Agent 1.0'
    })
    if response.status_code == 200:
        hot_list.extend(
          [i.get("data").get("title")
           for i in response.json().get("data").get("children")]
        )
        if response.json().get("data").get('after'):
            params["after"] = response.json().get("data").get('after')
            return recurse(subreddit, hot_list, params)

    return hot_list if hot_list else None
