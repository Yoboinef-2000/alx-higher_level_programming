#!/usr/bin/python3

"""
This python script takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import sys
from urllib import request

if __name__ == "__main__":
    theURL = sys.argv[1]
    with request.urlopen(theURL) as url:
        theURLheader = url.getheader('X-Request-Id')
        print(theURLheader)
