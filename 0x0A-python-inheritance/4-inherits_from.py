#!/usr/bin/python3

"""I have to include this line."""


def inherits_from(obj, a_class):
    """
    Return true if the object is an instance of a class that inherited.

    (directly or indirectly) from the specified class.

    Return false otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
