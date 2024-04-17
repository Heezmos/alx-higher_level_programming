#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text
    file using JSON representation.

    Args:
        my_obj: The Python object to
        be written to the file.
        filename (str): The name of the
        file to write to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
