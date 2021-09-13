#!/usr/bin/python3
"""script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress."""

import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    tds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    success = [task for task in tds if task['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], len(success), len(tds)))

    for task in success:
        print("\t" + task['title'])
