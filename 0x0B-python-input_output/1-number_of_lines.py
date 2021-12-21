#!/usr/bin/python3
"""Number of lines from a file"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    """
    nb_lines = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            nb_lines += 1
    return nb_lines
