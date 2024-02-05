#!/usr/bin/python3

"""The Lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    attrMeth = []
    for i in dir(obj):
        attrMeth.append(i)
    return attrMeth
