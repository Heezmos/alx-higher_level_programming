#!/usr/bin/python3
"""Defines an inherited
list of  class MyList."""


class MyList(list):
    """It Implements sorted printing
    for built-in list class."""

    def print_sorted(self):
        """Print a list in sorted climbing order."""
        print(sorted(self))
