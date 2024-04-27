#!/usr/bin/python3

"""
This python script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    theURL = sys.argv[1]
    try:
        with request.urlopen(theURL) as url:
            readURL = url.read().decode('utf-8')
            print(readURL)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
