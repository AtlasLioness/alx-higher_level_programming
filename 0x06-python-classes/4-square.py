#!/usr/bin/python3
"""Square"""


class Square:
    """defining square"""
    def __init__(self, size=0):
        """initialization function"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of square"""
        return self.__size ** 2
