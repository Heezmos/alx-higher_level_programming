#!/usr/bin/python3
"""Defines an object attribute
lookup function in the code."""


def lookup(obj):
    """Return the  list of an object available attributes."""
    return (dir(obj))
