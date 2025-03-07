#!/usr/bin/python3
def complex_delete(a_dict, value):
    ''''Deletes keys with a specific value in a dictionary.'''

    keys_to_delete = [key for key in a_dict if a_dict[key] == value]

    for key in keys_to_delete:
        del a_dict[key]

    return a_dict
