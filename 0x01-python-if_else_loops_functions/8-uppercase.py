#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()
