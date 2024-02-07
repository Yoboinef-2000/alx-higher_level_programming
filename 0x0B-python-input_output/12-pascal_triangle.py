#!/usr/bin/python3

"""I have to include this iine."""


def pascal_triangle(n):
    """Return a list of lists of integers representing the
    Pascal’s triangle of n."""
    if (n <= 0):
        return []
    pascallist = []
    for i in range(n):
        row = [1]

        if i > 0:
            rrow = pascallist[i - 1]
            for j in range(1, i):
                row.append(rrow[j - 1] + rrow[j])

            row.append(1)
        pascallist.append(row)

    return (pascallist)
