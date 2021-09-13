#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.

"""
import sys
import requests
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    tds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    data = []

    for task in tds:
        data.append([user['id'], user['username'],
                    task['completed'], task['title']])

    with open(str(user['id']) + ".csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
