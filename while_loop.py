#!/usr/bin/env python3

"""while loop script showing examples
with the first being a basic loop with else
the second using a break condition
and the last being a continue condition
"""

import time

num = 6
while num <= 10:
    print(num)
    time.sleep(1)
    num = num + 1
else:
    print(num)

time.sleep(2)

"""while loop still adding one to the var 2 until less 
than or equal to 10 but stoping the loop if var num is equal 
to 7 this is done in an if statement
"""

num = 2
while num <= 10:
    print(num)
    time.sleep(1)
    if num == 7:
        break
    num = num + 1

"""this is a continued
if passwd is not equal to icespice program will keep
asking for the passwd, once correctly typed in will 
print a message
"""

passwd = ""

while passwd != "icespice":
    passwd = input('enter the password: ')
    print('no try again')
print('lucky guess')





