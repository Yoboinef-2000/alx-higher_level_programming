#!/usr/bin/python3

"""Import json and os."""
import json
import csv
"""Base Class."""


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the string representation."""
        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation to a file."""
        if list_objs is None:
            list_objs = []
        className = cls.__name__
        fileName = className + ".json"
        with open(fileName, "w") as file:
            jsonStrs = []
            for jStrs in list_objs:
                jsonStrs.append(jStrs.__dict__)
            jsonStrs = json.dumps(jsonStrs)
            file.write(cls.to_json_string(jsonStrs))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attribures set."""
        if cls.__name__ == "Rectangle":
            isYouDumborIsYouDumb = cls(1, 1, 0, 0, None)
        elif cls.__name__ == "Sqaure":
            isYouDumborIsYouDumb = cls(1, 0, 0, None)
        else:
            isYouDumborIsYouDumb = cls()
        isYouDumborIsYouDumb.update(**dictionary)
        return (isYouDumborIsYouDumb)
