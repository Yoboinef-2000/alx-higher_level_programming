#!/usr/bin/python3

"""I have to have this line."""


def is_kind_of_class(obj, a_class):
    """
    Return true if the object is an instance of,
    or if the object is an instance of a class that
    it was innherited from.

    Return false otherwise."""

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
