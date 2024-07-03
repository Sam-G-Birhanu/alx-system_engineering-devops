#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'myapp0101'}
    url = f"https://www.reddit.com/r/funny/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Get number of subscribers
        subscribers = data['data']['subscribers']
        
        return subscribers
    return (0)
