#!/usr/bin/python3

"""I have to include this line."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and returns
    the number of characters written."""
    with open(filename, "w", encoding="utf-8") as ffile:
        writeFile = ffile.write(text)
        return (writeFile)
