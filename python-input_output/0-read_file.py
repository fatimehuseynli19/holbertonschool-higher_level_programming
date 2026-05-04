#!/usr/bin/python3
"""Module for reading a text file and printing it to stdout."""


def read_file(filename=""):
    """Read a text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
