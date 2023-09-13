#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """reads then prints text file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
