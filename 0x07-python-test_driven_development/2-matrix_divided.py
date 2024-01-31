#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Return a matrix divided by div."""
    divMatrix = []
    for i in matrix:
        if not isinstance(i, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        j = 0
        for j in range(len(i)):
            if not isinstance(j, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

