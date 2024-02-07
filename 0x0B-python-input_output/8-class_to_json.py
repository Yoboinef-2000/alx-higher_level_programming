#!/usr/bin/python3

"""I have to include this line."""


def class_to_json(obj):
    """Return the dictionary description with simple
    data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object."""
    return {key: value for key, value in obj.__dict__.items()}
