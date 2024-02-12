#!/usr/bin/python3

"""Import Rectangle."""
from rectangle import Rectangle

"""Square Class."""


class Square(Rectangle):
    """Sqaure Class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize and assign attributes."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override __str__ to return something diff."""
        # I am writing these extra lines so that I can
        # pass the pycodestyle checker. I hate this cloggy
        # look.
        idd = self.id
        xx = self.x
        yy = self.y
        sz = self.width

        return ("[Square] ({}) {}/{} - {}".format(idd, xx, yy, sz))

    @property
    def size(self):
        """Return size."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update and assign."""
        if len(args) > 0 and args[0] is not None:
            self.id = args[0]
        elif kwargs.get('id') is not None:
            self.id = kwargs['id']

        if len(args) > 1 and args[1] is not None:
            self.width = args[1]
            self.height = args[1]
        elif kwargs.get('size') is not None:
            self.width = kwargs['size']
            self.height = kwargs['size']

        if len(args) > 2 and args[2] is not None:
            self.x = args[2]
        elif kwargs.get('x') is not None:
            self.x = kwargs['x']

        if len(args) > 3 and args[3] is not None:
            self.y = args[3]
        elif kwargs.get('y') is not None:
            self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of Sqaure."""
        # return(self.__dict__)
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
