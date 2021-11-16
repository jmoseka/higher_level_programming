#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        if n == 8 or n == 9:
            print("{}{}".format(n, m))
        else:
            print("{}{}".format(n, m), end=", ")
