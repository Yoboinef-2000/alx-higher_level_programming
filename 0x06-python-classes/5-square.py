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
        self.__size = size

    def area(self):
        """Area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the area of the Square using #."""
        if (self.__size == 0):
            print()
        else:
            i = 0
            while (i < self.__size):
                j = 1
                while (j < self.__size):
                    j = j + 1
                    print("#", end="")
                print("#")
                i = i + 1
