#!/usr/bin/python3
for char in "zyxwvutsrqponmlkjihgfedcba":
    print(f"{char.lower() if char.isupper() else char.upper()}", end="")
