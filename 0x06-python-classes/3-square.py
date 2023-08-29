#!/usr/bin/python3
"""Square"""


class Square:
    """defining square"""
    def __init__(self, size):
        """initialization function"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2
