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
    users = requests.get(url + "users").json()
    tds = requests.get(url + "todos").json()

    data = {u['id']: [{'username': u['username'],
                       'task': t['title'],
                       'completed': t['completed']}
                     for t in tds if t['userId'] == u['id']]
            for u in users}

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
