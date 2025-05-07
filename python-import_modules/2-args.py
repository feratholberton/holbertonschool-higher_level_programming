#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]
    arguments_qty = len(arguments)

    if arguments_qty == 0:
        print('0 arguments.')
    elif arguments_qty == 1:
        print('1 argument:')
    else:
        print(f'{arguments_qty} arguments:')

    for counter, argument in enumerate(arguments, start=1):
        print(f'{counter}: {argument}')
