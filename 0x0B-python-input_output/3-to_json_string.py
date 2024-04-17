#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation
    of a string object.

    Args:
        my_obj: The object to be
        converted to JSON.

    Returns:
        str: A JSON representation of the input object.
    """
    return json.dumps(my_obj)
