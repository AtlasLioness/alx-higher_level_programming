#!/usr/bin/python3
"""Defines class Rectangle based on BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectange(BaseGeometry):
    """Class rectangle definition"""
    def __init__(self, width, height):
        """initializing rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
