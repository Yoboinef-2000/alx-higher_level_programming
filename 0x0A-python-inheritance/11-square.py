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


class Rectangle(BaseGeometry):
    """Rectangle Class."""

    def __init__(self, width, height):
        """Intialise width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the string representation."""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square Class."""

    def __init__(self, size):
        """Initialize size."""
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__width}"
