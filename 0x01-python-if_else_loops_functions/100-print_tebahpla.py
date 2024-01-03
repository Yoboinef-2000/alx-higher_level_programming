#!/usr/bin/python3
for char in "zyxwvutsrqponmlkjihgfedcba":
    print(char.upper() if char.islower() else char.lower(), end="")
