#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n < 0:
    last = ((n * -1) % 10) * -1
else:
    last = n % 10
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(n, last))
elif last < 6 and last != 0:
    print("Last Number of {} is {} and is less\
 than 6 and not 0".format(n, last))
