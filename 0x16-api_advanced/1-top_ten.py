#!/usr/bin/python3
""" comments """
import requests
import sys


def top_ten(subreddit):
    """ print top ten hot posts """
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    hot_list = requests.get(url, headers={'User-agent':
                            'robertrowe1013'}).json().get('data')
    if hot_list is None:
        print("None")
    else:
        hl_list = hot_list.get('children')
        i = 0
        while i < 10:
            title = hl_list[i].get('data').get('title')
            print(title)
            i += 1
