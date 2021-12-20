#!/usr/bin/python3
"""define a inherits_from function"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited

    Args:
       obj: object argument
       a_class: specified class

    Return:
       True or false
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
