#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    tds = requests.get(url + "todos").json()

    data = {u.get('id'): [{'username': u.get('username'),
                           'task': t.get('title'),
                           'completed': t.get('completed')}
                          for t in tds if t['userId'] == u['id']]
            for u in users}

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
