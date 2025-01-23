#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_length = len(sentence)

    if sentence_length == 0:
        sentence_first_letter = None
    else:
        sentence_first_letter = sentence[0]

    return (sentence_length, sentence_first_letter)
