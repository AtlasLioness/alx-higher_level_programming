#!/usr/bin/python3
"""defines function inherits_from()"""


def inherits_from(obj, a_class):
    """returns True if obj is subclass of a_class"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    else:
        return False
