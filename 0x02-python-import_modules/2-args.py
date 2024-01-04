#!/usr/bin/python3

import sys

args_count = len(sys.argv) - 1

if args_count == 0:
    print(".")
else:
    print("{} argument{}:".format(args_count, 's' if args_count > 1 else ''))
    for i in range(1, args_count + 1):
        print("{}: {}".format(i, sys.argv[i]))
