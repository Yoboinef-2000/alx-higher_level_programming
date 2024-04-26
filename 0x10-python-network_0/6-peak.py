#!/usr/bin/python3

"""Finds the peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers."""
    if list_of_integers:
        max = list_of_integers[0]
        for i in list_of_integers:
            if i > max:
                max = i

        return (max)
