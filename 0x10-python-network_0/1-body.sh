#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of th response
curl -s "$1" -X GET -L