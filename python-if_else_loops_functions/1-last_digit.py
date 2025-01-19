#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    compare_result = 'greater than 5'
elif last_digit == 0:
    compare_result = '0'
else:
    compare_result = 'less than 6 and not 0'

print(f'Last digit of {number} is {last_digit} and is {compare_result}')
