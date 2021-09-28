#!/usr/bin/python3
"""define the function count_words"""
import requests


def count_words(subreddit, word_list, params={}, counts={}):
    """
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, params=params, headers={
        'User-Agent': 'My User Agent 1.0'
    })
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            for word in list(map(lambda w: w.lower(), word_list)):
                title = i.get("data").get("title").lower().split(" ")
                if word in title:
                    if word in counts.keys():
                        counts[word] += title.count(word)
                    else:
                        counts[word] = title.count(word)

        if response.json().get("data").get('after'):
            params["after"] = response.json().get("data").get('after')
            count_words(subreddit, word_list, params, counts)
        else:
            for t in sorted([(k, v) for k, v in counts.items() if v],
                            key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(t[0], t[1]))
