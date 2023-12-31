#!/usr/bin/python3
"""Define rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """initiation method for rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
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
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns rectangle with character #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """returns string rep of rectangle to recreate a new instance"""
        string = "Rectangle("
        string += str(self.__width)
        string += ", " + str(self.__height) + ")"
        return string
