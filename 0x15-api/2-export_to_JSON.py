#!/usr/bin/python3
""" export """
import json
import requests
import sys


def json_export():
    """ exort to json """
    filename = sys.argv[1] + '.json'
    todo = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1] + '/todos').json()
    user_id = sys.argv[1]
    username = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            sys.argv[1]).json().get('username')
    json_dict = {user_id: [{"task": task.get('title'),
                 "completed": task.get('completed'),
                            "username": username} for task in todo]}

    with open(filename, 'w') as file:
        json.dump(json_dict, file)

if __name__ == "__main__":
    json_export()
