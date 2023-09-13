#!/usr/bin/python3
"""Module with save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to a texte file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
