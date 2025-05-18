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

    symbols = [":", "?", "."]

    for char in symbols:
        text = (char + "\n\n").join([x.strip(" ") for x in text.split(char)])

    print(f"{text}", end='')
