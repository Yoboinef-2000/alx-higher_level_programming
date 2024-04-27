#!/usr/bin/python3

"""
This Python script takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import sys
from urllib import request, parse

# if __name__ == "__main__":
#     theURL = sys.argv[1]
#     email = sys.argv[2]
#     encodeTheEmail = parse.urlencode({'email': email}).encode('utf-8')
#     with request.urlopen(theURL) as url:
#         readURL = url.read().decode('utf-8')
#         print(readURL)
if __name__ == "__main__":
    theURL = sys.argv[1]
    email = sys.argv[2]
    encodeTheEmail = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(theURL, data=encodeTheEmail) as url:
        readURL = url.read().decode('utf-8')
        print(readURL)

