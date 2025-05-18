#!/usr/bin/python3
'''
Inserts two newlines after '.', '?', and ':'
'''


def text_indentation(text):
    '''
    Prints `text` with 2 newlines after '.', '?', and ':'.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ''
    for char in text:
        current_line += char
        if char in '.?:':
            print(current_line.strip())
            print()
            current_line = ''
    if current_line.strip():
        print(current_line.strip())
