#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while(count < x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except (TypeError, ValueError):
                pass
            finally:
                i = i + 1
    except (IndexError):
        pass
    finally:
        print()
        return (count)
