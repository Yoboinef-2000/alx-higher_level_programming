#!/usr/bin/python3

"""Import json and csv."""
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

    @classmethod
    def load_from_file(cls):
        """Got this from mot. Hope it works."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as file:
                dict_list = Base.from_json_string(file.read())
                return [cls.create(**i) for i in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file."""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file to a list of instances."""
        filename = f"{cls.__name__}.csv"
        instances = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    instances.append(cls.from_csv_row(row))
        except FileNotFoundError:
            pass
        return (instances)

    def to_csv_row(self):
        """Convert object attributes to a CSV row."""
        chupapi = "to_csv_row method must be implemented in each subclass"
        raise NotImplementedError(chupapi)

    @classmethod
    def from_csv_row(cls, csv_row):
        """Create an instance from a CSV row."""
        chupapi = "from_csv_row method must be implemented in each subclass"
        raise NotImplementedError(chupapi)
