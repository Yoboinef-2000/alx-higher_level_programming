#!/usr/bin/python3

"""Import json."""
import json

"""I have to include this line."""


def load_from_json_file(filename):
    """Create an Object from a “JSON file”."""
    with open(filename, "r", encoding="utf-8") as file:
        createObjfile = json.load(file)
        return (createObjfile)
