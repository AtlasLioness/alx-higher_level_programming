#!/usr/bin/python3
"""Defines class Rectangle based on BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle definition"""

    def __init__(self, width, height):
        """initializing rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        string = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return string
