#!/usr/bin/python3
"""
A Python program that reads
and prints the
contents of a text file to stdout.
"""


def read_file(filename=""):
    """
    Reads the specified text file and
    prints its contents
    to the standard output (stdout).

    :param filename: The name of the text
    file to be read and printed.
    """
    if filename == "":
        return
    with open(filename, "r") as file:
        print(file.read(), end="")
