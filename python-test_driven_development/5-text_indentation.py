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

    # for char in symbols:
        # text = (char + "\n\n").join([x.strip(" ") for x in text.split(char)])

    # print(f"{text}", end='')


    i = 0
    while i < len(text):
        print(text[i], end='')

        if text[i] in symbols:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
