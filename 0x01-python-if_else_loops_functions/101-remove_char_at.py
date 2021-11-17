#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0):
        first_part = str[:n]
        last_part = str[n+1:]
        return first_part + last_part
    return str
