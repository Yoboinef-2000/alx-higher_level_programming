#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of th response

theURL="$1"
curl -s -X GET -L "$theURL"

# -X : As mentioned in the quiz and the course material for it, this option
# defines the HTTP method used. I need to put that thorugh my thick head.
# I think I will remember it if I start using it often.
# Which means I wont remember it ever.

# -L : Again, as mentioned in the quiz and the curl video I watched for it, this option
# is for following redirects.
# But ask me again, will I ever remember this flag?
# Yeah you guessed right!
# ;)