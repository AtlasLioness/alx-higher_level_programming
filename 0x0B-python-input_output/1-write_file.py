#!/usr/bin/python3
"""Module with pme function"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns nb of chars writter
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
