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

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """add the setter to the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """Public instance method that prints the square"""
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
