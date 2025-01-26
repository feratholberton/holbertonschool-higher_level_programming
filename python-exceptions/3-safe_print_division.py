#!/usr/bin/python3

def safe_print_list_integers(a, b):
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print('Inside result: {}').format(result)
    return result
