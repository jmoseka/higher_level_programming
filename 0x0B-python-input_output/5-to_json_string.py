#!/usr/bin/python3
"""define function To_JSON string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an obj"""
    return json.dumps(my_obj)
