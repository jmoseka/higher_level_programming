#!/usr/bin/python3
"""Defines MyList function"""


class MyList(list):
    """The __init__ method initialize"""
    def __init__(self):
        """empty class"""
        pass

    def print_sorted(self):
        """inherits from list"""
        print(sorted(self))
