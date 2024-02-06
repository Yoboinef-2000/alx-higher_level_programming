#!/usr/bin/python3

"""Import json."""
import json

"""I have to include this line."""


def save_to_json_file(my_obj, filename):
    """Write a string to a text file (json) and returns
    the number of characters written."""
    with open(filename, "w") as ffile:
        writeFile = json.dump(my_obj, ffile)
        return (writeFile)
