#!/usr/bin/python3
for y in range(ord('a'), ord('z') + 1):
    if y != ord('e') and y != ord('q'):
        print("{:c}".format(y), end="")
