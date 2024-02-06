#!/usr/bin/python3

"""I have to include this line."""


def write_file(filename="", mode="w", text=""):
    """Write a string to a text file (UTF8) and returns
    the number of characters written."""
    with open(filename, encoding="utf-8") as ffile:
        return (ffile.write(text))
