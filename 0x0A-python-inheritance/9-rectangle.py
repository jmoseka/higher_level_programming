#!/usr/bin/python3
"""
Creates a Rectangle class and import BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        method that return the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method that prints a rectangle description
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
