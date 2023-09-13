#!/usr/bin/python3
"""Module defining Student class"""


class Student:
    """defining Student Class"""
    def __init__(self, first_name, last_name, age):
        """instantiation of class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict reprensentation of a Student"""
        if attrs is None:
            return self.__dict__
        if (isinstance(attrs, list) and
                all(type(item) == str for item in attrs)):
            return {item: getattr(self, item)
                    for item in attrs if hasattr(self, item)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
