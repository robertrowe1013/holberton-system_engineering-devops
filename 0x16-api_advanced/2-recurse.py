#!/usr/bin/python3
""" comments """
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """ recursively get hot list items """
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    h_list = requests.get(url, headers={'User-agent':
                          'robertrowe1013'}).json().get('data')
    if h_list is None:
        return None
    else:
        hl_list = h_list.get('children')
        hl_len = len(hot_list)
        if hl_len < 10:
            hl_add = hl_list[hl_len].get('data').get('title')
            hot_list.append(hl_add)
            recurse(subreddit, hot_list)
        else:
            return hot_list
