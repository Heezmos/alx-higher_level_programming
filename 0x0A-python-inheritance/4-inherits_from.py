#!/usr/bin/python3
"""
A function that returns True if
the object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that
    has inherited from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        True if obj is an instance
        of a class that has
        inherited from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
