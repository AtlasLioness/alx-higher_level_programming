#!/usr/bin/python3
def safe_print_integer_err(value):

    result = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        result = False
        print("Exception: {}".format(e))
    return result
