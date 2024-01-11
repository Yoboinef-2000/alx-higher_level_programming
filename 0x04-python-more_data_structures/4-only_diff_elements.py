#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return set()

    diff_set_1 = set_1.difference(set_2)
    diff_set_2 = set_2.difference(set_1)
    result_set = diff_set_1.union(diff_set_2)

    return result_set
