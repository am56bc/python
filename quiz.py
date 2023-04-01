#!/usr/bin/env python3

import time

score = 0

def sleep():
    pause = time.sleep(2)
    print('your current score is ' + str(score))

print('Welcome to my quiz!')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Ok! Let's play!")

answer = input("What is my MN/KC nickname? ")
if answer.lower() == "ap":
    print('Correct')
    score += 1
else:
    print('Incorrect')

sleep()
answer = input("What is my COMO nickname? ")
if answer.lower() == "sevynn":
    print('Correct')
    score += 2
else:
    print('Incorrect')

sleep()
answer = input("How old am I turning this year? ")
if answer == "21":
    print('Correct')
    score += 1
else:
    print('Incorrect')

sleep()
answer = input("Are you single? ")
if answer.lower() == "yes":
    print('no need to brag :|')
    score += 1
else:
    print('lame b***h')

sleep()
answer = input("How many bodies do I have? ")
if answer == "7":
    print('Why do you know this again')
    score += 3
else:
    print('Incorrect')
print('your final score is ' + str(score))
