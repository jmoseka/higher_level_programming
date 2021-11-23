#!/usr/bin/python3
def no_c(my_string):
    if 'c' in my_string and 'C' in my_string:
        my_string = my_string.translate({ord('C'): None})
        my_string = my_string.translate({ord('c'): None})
        return my_string
    elif 'c' in my_string:
        my_string = my_string.translate({ord('c'): None})
        return my_string
    elif 'C' in my_string:
        my_string = my_string.translate({ord('C'): None})
        return my_string
    else:
        return my_string
