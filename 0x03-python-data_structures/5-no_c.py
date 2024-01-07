#!/usr/bin/python3

def no_c(my_string):
    i = 0
    newString = []
    for char in my_string:
        if char != 'c' and char != 'C':
            newString.append(char)
    return("".join(newString))
