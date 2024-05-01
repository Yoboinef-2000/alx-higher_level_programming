#!/usr/bin/python3

"""
This Python Script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    theURL = sys.argv[1]
    readURL = requests.get(theURL)
    if readURL.status_code >= 400:
        print("Error code: {}". format(readURL.status_code))
    else:
        print(readURL.text)
