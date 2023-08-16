#!/usr/bin/python3
def roman_to_int(roman_string):

    dictio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    comp = 0

    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) - 1, -1, -1):
            if dictio[roman_string[i]] >= comp:
                result += dictio[roman_string[i]]
            else:
                result -= dictio[roman_string[i]]
            comp = dictio[roman_string[i]]
    return result
