#!/usr/bin/env python3
'''
Define a Class that Extend the Python List with Notifications
'''


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f'Added [{item}] to the list.')

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f'Extended the list with [{count}] items.')

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f'Removed [{item}] from the list.')
        else :
            print(f'Item [{item}] not found in the list.')
    
    def pop(self, index=-1):
        if len(self) > 0:
            item = super().pop(index)
            print(f'Popped [{item}] from the list.')
            return item
        else:
            print('List is empty')
            return None
