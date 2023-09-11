#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Class with one attribute"""

    def area(self):
        """raises exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value if integer and positive"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
