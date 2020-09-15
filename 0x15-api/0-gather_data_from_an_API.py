#!/usr/bin/python3
""" gather data """
import requests
import sys


def todo_list():
    """ print todo list """
    name = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1]).json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1] + '/todos').json()
    total_tasks_count = len(todo)
    completed_tasks = []
    for task in todo:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    completed_tasks_count = len(completed_tasks)
    print("{} is done with tasks({}/{}):".format(name,
          completed_tasks_count, total_tasks_count))
    for task in completed_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    todo_list()
