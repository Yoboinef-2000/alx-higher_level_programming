#!/usr/bin/python3

def uniq_add(my_list=[]):
    i = 0
    j = 0
    summ = 0
    newList = []
    while i < len(my_list):
        if my_list[i] not in newList:
            newList.append(my_list[i])
        i += 1
    while j < len(newList):
        summ += newList[j]
        j += 1
    return summ
