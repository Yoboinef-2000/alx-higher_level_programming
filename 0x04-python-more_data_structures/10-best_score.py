#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    else:
        i = 0
        for element in a_dictionary:
            if i == 0:
                maxx = a_dictionary[element]
                el = element
                i += 1
            elif a_dictionary[element] > maxx:
                maxx = a_dictionary[element]
                el = element
        return el
