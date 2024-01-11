#!/usr/bin/python3

def common_elements(set_1, set_2):
    i = 0

    if set_1 is None or set_2 is None:
        return set()
    else:
        newList = []
        sett1 = list(set_1)
        sett2 = list(set_2)

        while (i < len(sett1)):
            j = 0
            while (j < len(sett2)):
                if (sett1[i] == sett2[j]):
                    newList.append(sett1[i])
                j += 1
            i += 1
        return newList
