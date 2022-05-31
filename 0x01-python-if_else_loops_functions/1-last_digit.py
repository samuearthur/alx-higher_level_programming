#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
z = abs(n) % 10
if n < 0:
    z = -z
print("Last digit of {} is {} and is ".format(number, z), end="")
if z > 5:
    print("greater than 5")
elif z == 0:
    print("0")
else:
    print("less than 6 and not 0")
