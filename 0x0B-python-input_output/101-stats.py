#!/usr/bin/python3

"""Import sys."""
import sys

"""I have to include this line."""


def print_statistics(total_size, status_code_counts):
    """Read stdin line by line and computes metrics."""
    print("File size:", total_size)
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")
