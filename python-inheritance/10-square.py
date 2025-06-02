#!/usr/bin/python3
''' Define a class Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

        # Call the parent class - Rectangle
        super().__init__(size, size)

    def area(self):
        ''' Calculates area '''
        return self.__size * self.__size
