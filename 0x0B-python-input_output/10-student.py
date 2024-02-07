#!/usr/bin/python3

"""I have to include this line."""


class Student():
    """Class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize self attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr, None) for attr in attrs}
        else:
            return {key: value for key, value in self.__dict__.items()}
