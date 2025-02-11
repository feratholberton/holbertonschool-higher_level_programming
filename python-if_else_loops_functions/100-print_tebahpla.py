#!/usr/bin/python3

print(''.join('{:c}'.format(i - (32 * (i % 2))) for i in range(122, 96, -1)), end='')