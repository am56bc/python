#!/usr/bin/env python3

"""This script file will have simple examples of
how to write a function
and scopes [local,global,enclosing]
"""


def name_function():
    """this is a fucntion that will ask what 
       is ur fav fruit and will print out
       apple
    """
    global apple
    apple = 'watermelon'
    print('what is ur favorite fruit?')
    print(apple)


name_function()
print(apple)
print('why twice? you weirdo')



x = 25

def quarter():
    global x
    x = 50
    quarter()
print(x)


