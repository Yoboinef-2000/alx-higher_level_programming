#!/usr/bin/python3

"""This is an empty Rectangle Class."""


class Rectangle:
    """This is an empty Rectangle Class."""

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        return ((str(self.print_symbol) * self.__width + "\n") * self.__height)

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangels and return the biggest one (Area wise)."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() > rect_2.area()) or (rect_1.area() == rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Class method to create a square with equal width and height."""
        return (cls(size, size))
