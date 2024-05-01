#!/usr/bin/python3

"""
This Python script take 2 arguments in order to solve this challenge:
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

import sys
import requests

if __name__ == "__main__":
    gitHubRepo = sys.argv[1]
    gitHubOwner = sys.argv[2]
    theRequest = requests.get('https://api.github.com/repos/{}/{}/commits'
                              .format(gitHubOwner, gitHubRepo))

    if theRequest.status_code >= 400:
        print('None')
    else:
        for ola in (c for c in theRequest.json()[:10]):
            print("{}: {}".format(ola['sha'], ola['commit']['author']['name']))
