#!/usr/bin/python3
''' Define lookup function '''


class MyList(list):
    ''' Returns a list of attributtes and methods of an object '''

    def print_sorted(self):
        print(sorted(self))
