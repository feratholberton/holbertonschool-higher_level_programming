#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]
    arguments_qty = len(arguments)
    counter = 1

    if arguments_qty == 0:
        print('0 arguments.')
    elif arguments_qty == 1:
        print('1 argument:')
    else:
        print(F'{arguments_qty} arguments:')

    for argument in arguments:
        print(F'{counter}: {argument}')
        counter += 1
