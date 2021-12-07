#!/usr/bin/python3
"""This function define a square by private instance attribute."""


class Square:
    """The __init__ method initialize the values passed to the object.
    Attributes:
        size: its a private attribute.
    """

    def __init__(self, size):
        self.__size = size
