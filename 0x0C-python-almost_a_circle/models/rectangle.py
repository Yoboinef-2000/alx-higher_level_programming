#!/usr/bin/python3

"""Import Base."""
from base import Base

"""Rectangle Class."""


class Rectangle(Base):
    """Rectangle Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize and assign attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width."""
        return (self.__width)

    @property
    def height(self):
        """Return height."""
        return (self.__height)

    @property
    def x(self):
        """Return x."""
        return (self.__x)

    @property
    def y(self):
        """Return y."""
        return (self.__y)

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return area of the rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """Print rectangle using #."""
        i = 0
        numberofXs = (self.__x) * " "
        numberofYs = (self.__y) * "\n"
        print("{}".format(numberofYs), end="")
        while (i < self.__height):
            j = 1
            print("{}".format(numberofXs), end="")
            while (j < self.__width):
                print("#", end="")
                j += 1
            print("#")
            i += 1

    def __str__(self):
        """Override __str__ to return something diff."""
        # I am writing these extra lines so that I can
        # pass the pycodestyle checker. I hate this cloggy
        # look.
        idd = self.id
        xx = self.__x
        yy = self.__y
        wdth = self.__width
        hght = self.__height

        return (f"[Rectangle] ({idd}) {xx}/{yy} - {wdth}/{hght}")

    def update(self, *args, **kwargs):
        """Update and assign."""
        if len(args) > 0 and args[0] is not None:
            self.id = args[0]
        elif kwargs.get('id') is not None:
            self.id = kwargs['id']

        if len(args) > 1 and args[1] is not None:
            self.__width = args[1]
        elif kwargs.get('width') is not None:
            self.__width = kwargs['width']

        if len(args) > 2 and args[2] is not None:
            self.__height = args[2]
        elif kwargs.get('height') is not None:
            self.__height = kwargs['height']

        if len(args) > 3 and args[3] is not None:
            self.__x = args[3]
        elif kwargs.get('x') is not None:
            self.__x = kwargs['x']

        if len(args) > 4 and args[4] is not None:
            self.__y = args[4]
        elif kwargs.get('y') is not None:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of Rectangle."""
        # return(self.__dict__)
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
