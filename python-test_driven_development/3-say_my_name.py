#!/usr/bin/python3
"""
Module for say_my_name function.
This module prints a person's full name.
It validates that inputs are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.
    Raises TypeError if inputs are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
