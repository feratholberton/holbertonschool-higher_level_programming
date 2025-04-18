#!/usr/bin/python3
'''
This is a placeholder template for module docs
'''


def pascal_triangle(n):
    '''
    This is a placeholder template for function docs
    '''
    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1] * (row_num + 1)

        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle
