#!/usr/bin/python3
""" export """
import csv
import requests
import sys


def csv_export():
    """ export to csv """
    filename = sys.argv[1] + '.csv'
    todo = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        sys.argv[1] + '/todos').json()
    user_id = sys.argv[1]
    username = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            sys.argv[1]).json().get('username')
    row_list = []
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            tcs = task.get('completed')
            task_title = task.get('title')
            writer.writerow([user_id, username, tcs, task_title])

if __name__ == "__main__":
    csv_export()
