#!/usr/bin/env python3

# for letter in range(122, 96, -1):
#     if letter % 2 != 0:
#         letter = letter + 32

#     print('{}'.format(chr(letter)), end='')

print(''.join('{:c}'.format(i - (32 * (i % 2))) for i in range(122, 96, -1)))