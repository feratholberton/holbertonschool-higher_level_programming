#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    compared_result = 'greater than 5'
elif last_digit == 0:
    compared_result = '0'
else:
    compared_result = 'less than 6 and not 0'

print(f'Last digit of {number} is {last_digit} and is {compared_result}')
