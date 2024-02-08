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
            raise TypeError("{} must be an integer".format(name))
        if int(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle Class."""

    def __init__(self, width, height):
        """Intialise width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
