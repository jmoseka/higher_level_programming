#!/usr/bin/python3
"""define a is_same_class function"""

def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance
    of the specified class ; otherwise False."""
    if type(obj)is a_class:
        return True
    else:
        return False
