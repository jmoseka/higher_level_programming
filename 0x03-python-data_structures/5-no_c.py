#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if x == 'C':
            return my_string.translate({ord('C'):None})
        elif x == 'c':
            return my_string.translate({ord('c'):None})
