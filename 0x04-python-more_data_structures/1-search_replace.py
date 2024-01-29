#!/usr/bin/python3
"""
function that replaces all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    def find_search(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
