#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.

"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    tds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    data = []

    for task in tds:
        data.append([user.get('id'), user.get('username'),
                    task.get('completed'), task.get('title')])

    with open(str(user.get('id')) + ".csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
