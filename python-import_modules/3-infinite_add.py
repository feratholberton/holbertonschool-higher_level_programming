#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_numbers = sys.argv[1:]
    result = 0
    for number in arg_numbers:
        result += int(number)

    print(result)
