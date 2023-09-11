#!/usr/bin/python3
"""Defines function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if object is exactly an instance of class"""
    return type(obj) == a_class
