#!/usr/bin/python3

"""I have to include this line."""


def read_file(filename=""):
    """Open file with the with keyword."""
    with open(filename, encoding="utf-8") as ffile:
        readFile = ffile.read()
        print(readFile, end="")
