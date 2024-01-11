#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdict = {}
    for element in a_dictionary:
        newdict[element] = a_dictionary[element] * 2
    return newdict
