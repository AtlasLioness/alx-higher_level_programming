#!/usr/bin/python3
def safe_print_integer_err(value):

    result = True
    try:
        print("{:d}".format(value))
    except Exception:
        result = False
        return result
    else:
        return result


