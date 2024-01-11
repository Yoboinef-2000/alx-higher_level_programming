#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        totalsum = 0
        isdividedby = 0
        for i in my_list:
            totalsum = totalsum + (i[0] * i[1])
            isdividedby = isdividedby + i[1]
        return totalsum/isdividedby
