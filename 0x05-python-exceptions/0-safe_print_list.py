#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    i = 0
    nb_print = 0

    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_print += 1
        except Exception:
            continue
    print()
    return nb_print
