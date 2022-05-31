#!/usr/bin/python3
import random
v = random.randint(-10000, 10000)
if v < 0:
    lx = -v% 10
    lx = -lx
else:
    lx = v % 10
    if lx > 5:
        print("Last digit of {} is {} and is greater than 5".format(v, lx))
    elif lx < 6 and lx != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(v, lx))
    elif lx == 0:
        print("Last digit of {} is {} and is 0".format(v, lx))
