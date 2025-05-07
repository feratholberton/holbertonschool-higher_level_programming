#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv
    arguments_qty = len(arguments)

    if arguments_qty == 1:
        print('0 arguments.')
    elif arguments_qty == 2:
        counter = 1
        print('1 arguments:')
        for argument in arguments[1:]:
            print(F'{counter}: {argument}')
            counter += 1
    else:
        counter = 1
        print(F'{arguments_qty - 1} arguments.')
        for argument in arguments[1:]:
            print(F'{counter}: {argument}')
            counter += 1
