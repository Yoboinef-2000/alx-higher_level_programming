#!/usr/bin/python3

def common_elements(set_1, set_2):
    i = 0
    j = 0
    newList = []
    sett1 = list(set_1)
    sett2 = list(set_2)

    while i < len(sett1):
        while j < len(sett2):
            if (sett1[i] == sett2[j]):
                newList.append(sett1[i])
            j += 1
        i += 1
    return newList
