#!/usr/bin/python3

"""Finds the peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers."""
    if list_of_integers:
        low = 0
        high = len(list_of_integers) - 1

        while low < high:
            mid = (low + high) // 2

            if list_of_integers[mid] < list_of_integers[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return list_of_integers[low]
