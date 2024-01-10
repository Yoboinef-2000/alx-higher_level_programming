#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    i = 0
    j = 0

    sett1 = list(set_1)
    sett2 = list(set_2)

    while (i < len(sett1)):
        while (j < len(sett2)):
            if (sett1[i] == sett2[j]):
                del sett1[i]
                del sett2[j]
            j += 1
        i += 1
    newList = sett1 + sett2
    return (newList)
