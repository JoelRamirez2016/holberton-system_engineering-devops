#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""
import sys
import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    tds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    data = {user['id']: [{'task': t['title'], 'completed': t['completed'],
                          'username': user['username']} for t in tds]}

    with open(str(user['id']) + ".json", "w") as f:
        json.dump(data, f)
