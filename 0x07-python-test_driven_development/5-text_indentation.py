#!/usr/bin.python3

def text_indentation(text):
    """
    Print two lines after encountering certain special
    characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    alteredtext = ""
    divas = ['.', '?', ':']
    for i in text:
        alteredtext += i
        if i in divas:
            alteredtext += "\n\n"
    print(alteredtext)

