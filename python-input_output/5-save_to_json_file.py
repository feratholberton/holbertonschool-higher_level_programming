#!/usr/bin/python3
'''
This is a placeholder template for module docs
'''
import json


def from_json_string(my_obj, filename):
    '''
    This is a placeholder template for function docs
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
