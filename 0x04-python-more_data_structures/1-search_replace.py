#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    newlist = my_list.copy()
    while i < len(newlist):
        if search in newlist:
            newlist[newlist.index(search)] = replace
        i += 1
    return newlist
