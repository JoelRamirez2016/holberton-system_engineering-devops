#!/usr/bin/python3
"""define the function number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """
    result = 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={
        'User-Agent': 'My User Agent 1.0'
    })

    if response. status_code == 200:
        result = response.json().get("data").get("subscribers") 

    return result
