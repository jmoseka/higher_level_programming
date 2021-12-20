#!/usr/bin/python3
"""define a is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    check if object is an instance of,

    Args:
       obj: obj argument
       a_class: a_class to validate

    Return:
       True or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
