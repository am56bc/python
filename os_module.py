#!/usr/bin/env python3

#os module, some examples of common functions

"""this is checking working dir and using the 
os.system module to run the command ls to display
contents of that dir path
"""

import os

print("my current working directory is: " + os.getcwd() + "\n")

print("the contents of this working dir is: ")

os.system('ls')

"""this is checking if a file exists using the input function
wrote in an if statement, if file is not ther will make the file
using the os.system module again to touch that file name that was input
in the input
"""

file = input("enter a file: ")

if os.path.isfile(file):
    print("file exists")
else:
    print('file not there')
    print('making tho...')
    os.system('touch {}'.format(file))

path = os.path.abspath(input("input a file name: "))
print(path)
