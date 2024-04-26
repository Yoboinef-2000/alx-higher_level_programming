#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response

theURL="$1"
curl -s -X DELETE "$theURL"