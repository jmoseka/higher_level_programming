#!/usr/bin/python3
"""This function define a square by private instance attribute."""


class Square:
    """The __init__ method initialize the values passed to the object.
    Attributes:
        size: its a private attribute.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
