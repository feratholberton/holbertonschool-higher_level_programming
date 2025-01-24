#!/usr/bin/python3

def max_integer(my_list=[]):
    result = []

    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
