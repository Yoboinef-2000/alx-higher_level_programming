#!/usr/bin/python3

"""I have to include this iine."""


def pascal_triangle(n):
    """Return a list of lists of integers representing the
    Pascal’s triangle of n."""
    if (n <= 0):
        return {}
    else:
        pascallist = [] * n
        i = 0
        while (i < n/2):
            pascallist[i] = 1 + i
            pascallist[n - i] = 

