#!/usr/bin/env python3

"""this is working with files, first one is asking for the file name
and trying to open that file in the read format if it is not found it 
will print the file is not found as well as the error message if it is 
found it will print the contents of that file
"""

myfile = input("enter file name: ")
try:
    file = open(myfile)
except FileNotFoundError as e:
    print("file is not found") 
    print(e)
    exit(1)
for line in file:
    print(line)

soda = ["coca cola", "pepsi", "sprite", "sierra mist"]

for s in soda:
    file.write(s + "\n")
file.close()



