#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""
import json
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    tds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    data = {user.get('id'): [{'task': t.get('title'),
                              'completed': t.get('completed'),
                              'username': user.get('username')} for t in tds]}

    with open(str(user.get('id')) + ".json", "w") as f:
        json.dump(data, f)
