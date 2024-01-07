#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if (tuple_a[0] == None):
            tuple_a[0] = 0
        else:
            tuple_a[1] = 0
    if len(tuple_b) < 2:
        if (tuple_b[0] == None):
            tuple_b[0] = 0
        else:
            tuple_b[1] = 0
    newtuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (newtuple)
