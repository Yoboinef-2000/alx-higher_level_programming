#!/usr/bin/python3

"""Import importlib."""
import importlib
import sys

"""I have to include this line."""


saveJson = importlib.import_module('5-save_to_json_file')
loadJson = importlib.import_module('6-load_from_json_file')


def main():
    """Order main function."""
    data = loadJson.load_from_json_file("add_item.json")
    data.extend(sys.argv[1:])
    saveJson.save_to_json_file(data, "add_item.json")
