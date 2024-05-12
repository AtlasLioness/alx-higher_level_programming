#!/usr/bin/python3
""" Module that finds peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function to find a peak in a list of ints """
    li = list_of_integers
    if li == []:
        return None
    length = len(li)

    start = 0
    end = length - 1

    while start < end:
        half = start + (end - start) // 2
        if li[half] > li[half - 1] and li[half] > li[half + 1]:
            return li[half]
        if li[half - 1] > li[half + 1]:
            end = half
        else:
            start = half + 1
    return li[start]
