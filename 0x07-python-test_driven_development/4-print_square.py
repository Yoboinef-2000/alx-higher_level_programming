#!/usr/bin/python3

def print_square(size):
    """Print square using #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0: 
        raise ValueError("size must be >= 0")
    i = 0
    while (i < size):
        j = 0
        while (j < size):
            print("#",end="")
            j = j + 1
        print("")
        i = i + 1
