#!/usr/bin/python3
""" Define a custom class MyInt that inherits from int """


class MyInt(int):
    """ A custom integer class that changes the
    behavior of equality operators.
    """

    def __eq__(self, other):
        """ Override the equality operator (==) to
        return not equals (!=).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Override the not equals operator (!=)
        to return equals (==).
        """
        return super().__eq__(other)
