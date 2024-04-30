#!/usr/bin/python3

"""
This Python Scripttakes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    theURL = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post(theURL, data={'q': q})
    try:
        theDict = r.json()
        if theDict == {}:
            print('No result')
        else:
            print("[{}] {}".format(theDict.get('id'), theDict.get('name')))
    except ValueError:
        print('Not a valid JSON')
