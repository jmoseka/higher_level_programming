#!/usr/bin/python3
"""
define a square class and import Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        method that return the area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        method that prints a square description
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
