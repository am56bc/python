#!/usr/bin/env python3

import random

#random number
num = random.randint(50, 100)
print(num)

#random option
chips = ['hot fries', 'takis', 'pringles', 'ruffles']
types = random.choice(chips)
print(types)

#shuffle the items in the list
cars = ['jeep', '15', '18', '19', '20', 'bmw', 'benz', 'kia']
random.shuffle(cars)
print(cars)

#random amount for the list that do not repeat
num = [1,2,3,4,5]
random = random.sample(num, 2)
print(random)
