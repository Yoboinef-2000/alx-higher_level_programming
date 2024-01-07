#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        char = None
    else:
        char = sentence[0]
    comboTuple = (len(sentence), char)
    return (comboTuple)
