#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = [[]]
    for i in matrix:
        for j in range(i):
            newmatrix[i][j] = matrix[j] * matrix[j]

    return newmatrix
