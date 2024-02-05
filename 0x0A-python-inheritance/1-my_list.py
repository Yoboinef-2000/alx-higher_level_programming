#!/usr/bin/python3

"""Inheritance."""

class MyList(list):
    """MyList inherits from list."""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        getreckedNoImeangetSorted = sorted(self)
        print(getreckedNoImeangetSorted)
