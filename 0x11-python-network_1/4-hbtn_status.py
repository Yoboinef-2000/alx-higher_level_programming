#!/usr/bin/python3

"""This Python Script fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    theURL = "https://alx-intranet.hbtn.io/status"
    url = requests.get(theURL)
    readURL = url.text
    print("Body response:")
    print("\t- type: {}".format(type(readURL)))
    print("\t- content: {}".format(readURL))
