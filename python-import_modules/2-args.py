#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv
    arguments_qty = len(arguments)

    if arguments_qty == 1:
        print('0 arguments.')
    else:
        counter = 1
        for argument in arguments[1:]:
            print(F'{counter}: {argument}')
            counter += 1
