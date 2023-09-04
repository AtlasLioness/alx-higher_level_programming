#!/usr/bin/python3
"""Defines rectangle class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initiation method for rectangle size"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle peri;eter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
