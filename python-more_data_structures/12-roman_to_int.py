#!/usr/bin/python3
def roman_to_int(roman_string):
    ''' Converts a Roman numeral to an integer.'''

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Roman values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Process reversed values
    for numeral in reversed(roman_string):
        value = roman_values.get(numeral, 0)
        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total
