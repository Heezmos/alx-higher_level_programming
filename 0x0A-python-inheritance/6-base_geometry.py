#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    A class named BaseGeometry with
    an empty method named area.

    Methods:
    - area(): A public instance method that
    is not implemented.
    It raises an Exception when called.
    """
    def area(self):
        """A public instance method that is not implemented."""
        raise Exception("area() is not implemented")
