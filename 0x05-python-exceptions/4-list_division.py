#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    i = 0
    new_list = []

    for i in range(0, list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            i = i + 1

        except TypeError:
            print("wrong type")
            new_list[i] = 0
            continue

        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue

        except IndexError:
            print("out of range")
            new_list.append(0)
            continue

        finally:
            continue
    return new_list