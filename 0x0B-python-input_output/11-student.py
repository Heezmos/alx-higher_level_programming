#!/usr/bin/python3
"""Defines a class Student for representing student
information."""


class Student:
    """Represent a student.

    Attributes:
        first_name (str): The first name
        of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name
            of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list of str, optional): A list of
            attribute names to include
                in the dictionary representation.
                If None, all attributes are
                included.

        Returns:
            dict: A dictionary representation
            of the Student with specified
                attributes.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the
        Student with the provided JSON dictionary.

        Args:
            json (dict): A dictionary with key/value
            pairs to replace the
                attributes of the Student.
        """
        for k, v in json.items():
            setattr(self, k, v)
