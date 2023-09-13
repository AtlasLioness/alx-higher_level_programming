#!/usr/bin/python3
"""Module defining Student class"""


class Student:
    """defining Student Class"""
    def __init__(self, first_name, last_name, age):
        """instantiation of class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict reprensentation of a Student"""
        return self.__dict__
