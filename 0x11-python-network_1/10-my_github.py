#!/usr/bin/python3

"""
This Python script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import sys
import requests

if __name__ == "__main__":
    theRequest = requests.get('https://api.github.com/user',
                              auth=(sys.argv[1], sys.argv[2]))
    if theRequest.status_code >= 400:
        print('None')
    else:
        print(theRequest.json().get('id'))
