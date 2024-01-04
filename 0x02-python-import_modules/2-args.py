#!/usr/bin/python3

import sys

argsnum = len(sys.argv)

if argsnum == 2:
    print("1 argument:")
elif argsnum > 2:
    print("{} arguments:".format(argsnum - 1))

for i in range(argsnum):
    if i != 0:
        print("{}: {}".format(i, sys.argv[i]))
