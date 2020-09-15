#!/usr/bin/python3
""" export all employees """
import json
import requests
import sys


def json_export_all():
    """ export to json """
    pep8_cut = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    json_dict = {user.get("id"):
                 [{"task": task.get("title"),
                   "completed": task.get("completed"),
                   "username": user.get("username")}
                  for task in requests.get(pep8_cut,
                                           params={"userId":
                                                   user.get("id")}).json()]
                 for user in users}

    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)

if __name__ == "__main__":
    json_export_all()
