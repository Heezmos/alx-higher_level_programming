#!/usr/bin/python3
"""Defines a file-appending
function."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8
    encoded text file.

    Args:
        filename (str): The name of
        the file to
        which the text will be appended.
        text (str): The string to
        append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
