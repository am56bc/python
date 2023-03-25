#!/usr/bin/env python3

"""this is an if statement script 
with the less proactive scripts first
this first one is having basic input of a number and changing the var num
to and int so you can compare in the if statement
"""
import time

num = input("enter a number: ")

if int(num) < 10:
    print("this number is less than 10")

print("this will always print")

"""this is having an else statement if the first condition is not met
"""
time.sleep(4)

num = input("enter a number between 1 and 10: ")

if int(num) <= 10:
    print("valid number was entered")
else:
    print('not a valid response')

print("this will always print")

time.sleep(4)

"""this is displaying various outputs based on
if the conditions are met or not
""" 

age = input("enter ur age: ")

if int(age) >= 65:
    print('you are 65 or older')
elif int(age) >= 18:
    print('you are an adult')
else:
    print('you are not an adult')

print('this will always print')


amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)



one = "player 1 wins"
two = "player 2 wins"
options = "rock, paper, or scissors?: "
player1 = input(options)
player2 = input(options)


if player1 == player2:
    print('its a tie')
elif player1 == 'rock' and player2 == 'paper':
    print(one)
elif player1 == 'rock' and player2 == 'scissors':
    print(one)
elif player1 == 'paper' and player2 == 'rock':
    print(two)
elif player1 == 'paper' and player2 == 'scissors':
    print(two)
elif player1 == 'scissors' and player2 == 'rock':
    print(two)
else:
    print('something went wrong')


