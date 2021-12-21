#!/usr/bin/python3
"""definea a function"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        counter = 0
        for line in f:
            if counter < nb_lines:
                print(line, end="")
            elif not nb_lines or nb_lines < 0:
                print(line, end="")
            counter += 1
