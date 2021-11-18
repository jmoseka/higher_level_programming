#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    num = len(argv)
    for i in range(1, num):
        sum += int(argv[i])
    print("{}".format(sum))
