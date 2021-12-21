#!/usr/bin/python3
"""define a class Student"""


class Student:
    """defines a student by:

    Attributes:
        first_name: public instance
        last_name: public instance
        age: public instance
    """
    def __init__(self, first_name, last_name, age):
        """initialize object attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            names = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    names[key] = value
            return names
