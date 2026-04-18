#!/usr/bin/python3
"""
Module for print_square function.
This module prints a square using # character.
It validates that size is a non-negative integer.
"""


def print_square(size):
    """
    Prints a square with the character #.
    Size must be a non-negative integer.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
