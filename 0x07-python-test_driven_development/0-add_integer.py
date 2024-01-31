#!/usr/bin/python3

"""This is a simple add funtion."""


def add_integer(a, b=98):
    """Return sum."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = float(a)
    b = float(b)
    return (int(a + b))
