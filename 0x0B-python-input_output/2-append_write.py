#!/usr/bin/python3

"""I have to include this line."""


def append_write(filename="", text=""):
    """Write a string to a text file (UTF8) and returns
    the number of characters added."""
    with open(filename, "a", encoding="utf-8") as ffile:
        appendFile = ffile.write(text)
        return (appendFile)
