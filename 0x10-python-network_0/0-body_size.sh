#!/usr/bin/env bash
# This bash script takes in a URL, sends a request to that URL, and displays the size of the body of the response.

theURL="$1"
curl -s -o /dev/null -w "%{size_download}\n" "$theURL"

# -s: Silent mode - Option that operates silently without showing the progress information
# -w : Output format
# {size_download} : displays the size of the downloaded content in bytes