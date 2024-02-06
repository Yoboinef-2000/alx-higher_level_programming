#!/usr/bin/python3

"""I have to include this line."""


class BaseGeometry:
    """Geometry Class."""

    def area(self):
        """Raise an exception message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise more exception messages."""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if int(value) <= 0:
            raise ValueError("<name> must be greater than 0")
