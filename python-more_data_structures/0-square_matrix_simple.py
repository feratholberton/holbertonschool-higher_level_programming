#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for item in row:
            new_matrix.append(item*item)
        # new_matrix.append(row)

    return new_matrix