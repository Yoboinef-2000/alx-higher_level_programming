#!/usr/bin/python3

import sys

if __name__ == "__main__":

    argsnum = len(sys.argv)
    summ = 0
    for i in range(1, argsnum):
        summ += int(sys.argv[i])

    print(summ)
