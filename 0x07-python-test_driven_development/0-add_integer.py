#!/usr/bin/python3
"""
The "0-add_integer" module
with one function add_integer()

"""


def add_integer(a, b=98):
    """
    Returns sum of 2 numbers
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
