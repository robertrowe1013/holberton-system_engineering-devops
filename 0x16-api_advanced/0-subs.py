#!/usr/bin/python3
""" comments """
import requests
import sys


def number_of_subscribers(subreddit):
    """ print number of subs """
    sub_list = requests.get('https://reddit.com/r/' + subreddit + '/about/.json', headers = {'User-agent': 'robertrowe1013'}).json().get('data')
    if sub_list is None:
        return (0)
    sl_count = sub_list.get('subscribers')
    return (sl_count)
