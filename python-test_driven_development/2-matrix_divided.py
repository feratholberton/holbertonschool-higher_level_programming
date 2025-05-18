#!/usr/bin/python3
'''
This module is a function to divide all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    # Divides all elements by a number.
    '''
    mtx_x_msg = 'matrix must be a matrix (list of lists) of integers/floats'

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError(mtx_x_msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(num / div, 2) for num in row] for row in matrix]
