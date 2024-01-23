#!/usr/bin/python3

"""This is a square class."""


class Square:
    """This is a square class."""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """Area of the square."""
        return (self.__size * self.__size)
