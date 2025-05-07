#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_numbers = sys.argv[1:]
    print(sum(int(num) for num in arg_numbers))
