#!/usr/bin/python3
''' Define a Square class '''


class Square:
    ''' Square class '''

    def __init__(self, size=0):
        ''' Initiate Square instance'''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
