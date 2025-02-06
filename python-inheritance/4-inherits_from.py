#!/usr/bin/python3
''' Define a function '''


def inherits_from(obj, a_class):
    ''' Inherits from '''
    return isinstance(obj, a_class) and type(obj) is not a_class