#!/usr/bin/python3
'''
This Module define a square
'''


class Square:
    '''
    Square Class with private Size Attribute
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for row in range(self.__size):
                print('#' * self.__size)
