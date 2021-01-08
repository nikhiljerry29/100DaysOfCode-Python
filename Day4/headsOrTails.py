"""
You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".

e.g.
1 means Heads
0 means Tails
"""
import random

print("Welcome to the Virtual Coin Toss")
print("And it's a", end = " ")
tossValue = random.randint(0,1)
if tossValue == 1:
  print("Heads!!")
else:
  print("Tails!!")

