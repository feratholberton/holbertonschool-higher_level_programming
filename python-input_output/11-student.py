#!/usr/bin/python3
'''
This is a placeholder template for module docs
'''


class Student:
    '''
    This is a placeholder template for class docs
    '''

    def __init__(self, first_name, last_name, age):
        '''
        This is a placeholder template for function docs
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        This is a placeholder template for function docs
        '''
        if isinstance(attrs, list):
            return {
                key: getattr(self, key)
                for key in attrs
                if isinstance(key, str) and hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        '''
        This is a placeholder template for function docs
        '''
        for key in json:
            setattr(self, key, json[key])