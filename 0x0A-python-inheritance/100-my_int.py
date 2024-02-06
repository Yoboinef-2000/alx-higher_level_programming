#!/usr/bin/python3

"""I have to include this line."""


class MyInt(int):
    """This class inherits from the int class."""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)
