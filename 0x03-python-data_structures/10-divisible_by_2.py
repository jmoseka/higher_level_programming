#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for num in my_list:
        if num % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result
