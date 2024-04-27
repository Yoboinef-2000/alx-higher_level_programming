#!/usr/bin/python3

"""
This Python Script takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == "__main__":
    theURL = sys.argv[1]
    readURL = requests.get(theURL)
    theID = readURL.headers.get('X-Request-Id')
    print(theID)
