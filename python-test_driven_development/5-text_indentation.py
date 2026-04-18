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
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        elif i == 0 or text[i - 1] in ".?:":
            print(text[i], end="")
        else:
            print(text[i], end="")
        i += 1
