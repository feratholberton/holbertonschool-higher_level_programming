#!/usr/bin/python3
'''
This module adds 2 integers
'''


def add_integer(a, b=98):
    ''' 
    Adds 2 integers

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer('4', 5)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(4, 'school')
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
