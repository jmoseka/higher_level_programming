#!/usr/bin/python3
"""
Creates a BaseGeometry class
"""

class BaseGeometry:
    """
    Public instance method that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
