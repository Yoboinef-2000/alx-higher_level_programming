#!/usr/bin/python3

"""Import the urllib modeule."""
from urllib import request

if __name__ == "__main__":
    theURL = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(theURL) as url:
        readURL = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(readURL)))
        print("\t- content: {}".format(readURL))
        print("\t- utf8 content: {}".format(readURL.decode('utf-8')))
