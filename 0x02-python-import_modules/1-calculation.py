#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    summ = add(a, b)
    difference = sub(a, b)
    prada = mul(a, b)
    quot = div(a, b)

    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, difference))
    print("{} * {} = {}".format(a, b, prada))
    print("{} / {} = {}".format(a, b, quot))
