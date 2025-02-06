#!/usr/bin/python3
''' Define a class '''


class BaseGeometry:
    ''' Empty Base geometry '''
    def area(self):
        raise Exception('area() is not implemented')
