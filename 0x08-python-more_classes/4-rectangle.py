#!/usr/bin/python3

"""This is an empty Rectangle Class."""


class Rectangle:
    """This is an empty Rectangle Class."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle class."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width Getter."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width Setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height Setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (("#" * self.__width + "\n") * self.__height)

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
