from itertools import count
import random
import math
from typing import Counter
lowerLimit = int(input("Enter Lower limit:"))
upperLimit = int(input("Enter Upper limit:"))

x = random.randint(lowerLimit, upperLimit)
print("\n Total", round(math.log(upperLimit - lowerLimit + 1, 2)),
      "chances are there \n")

counter = 0
while Counter < math.log(upperLimit - lowerLimit + 1, 2):
 count += 1
 Guess = int(input("Guess a number:- "))
 if x == Guess:
    print("yeyyyy , you guessed the number correctly in ", count, "attempts")
 elif x > Guess:
    print("You guessed too small!")
 elif x < Guess:
    print("You Guessed too high!")

if count >= math.log(upperLimit - lowerLimit + 1, 2):
	print("\n Maximum attempts reached , better luck next time :( \n")
print("The number was :- ",x)
