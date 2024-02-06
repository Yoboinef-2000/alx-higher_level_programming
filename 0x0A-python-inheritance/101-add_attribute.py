#!/usr/bin/python3

"""I have to include this line."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if it’s possible."""
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
