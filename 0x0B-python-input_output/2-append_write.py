#!/usr/bin/python3
"""Module of append function"""


def append_write(filename="", text=""):
    """appends a string to text file & returns nb chars added"""
    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)
