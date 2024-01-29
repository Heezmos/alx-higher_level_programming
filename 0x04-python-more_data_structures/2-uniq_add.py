#!/usr/bin/python3
"""
function that adds all unique integers in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    number = 0
    for element in set(my_list):
        number += element
    return number
