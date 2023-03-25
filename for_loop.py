#!/usr/bin/env python3


"""for loop script
first showing that a string is also a list so this will print 
each letter on seperate line
"""


dell = "i am self learning"
for n in dell:
    print(n)

"""will set each list item to n in names list 
and print each item on a loop till its done 
"""

names = ['ify', 'ivo', 'ashley', 'amanda']
for n in names:
    print(n)

"""this is importing the module random and setting a range of numbers
from 5-10 to the var counter and setting num to 1. the range module is will generate
a random number wihtin those parameters. it will print from 1 to that random number
"""
import random

counter = random.randint(5, 10)
num = 1

for n in range(counter):
    print(num)
    num = num + 1


