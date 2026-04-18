#!/usr/bin/python3
"""
Module for text_indentation function.
This module prints text with 2 newlines after . ? and : characters.
It validates that text is a string.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each . ? and : character.
    No spaces at beginning or end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for ch in text:
        result += ch
        if ch in ".?:":
            result += "\n\n"
    for line in result.split("\n"):
        print(line.strip())
