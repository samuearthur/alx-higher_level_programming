#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lx = -number % 10
    lx = -ldigit
else:
    lx = number % 10
    if lx > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, lx))
    elif lx < 6 and lx != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, lx))
    elif lx == 0:
        print("Last digit of {} is {} and is 0".format(number, lx))
