#!/usr/bin/python3
''' Define a class Rectangle'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculates area '''
        return self.__width * self.__height

    def __str__(self):
        ''' String representation '''
        return f'[Rectangle] {self.__width}/{self.__height}'
