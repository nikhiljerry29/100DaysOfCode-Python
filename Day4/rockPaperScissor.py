"""
Rock Paper Scissor Game.
You have to manually input your choice and computer will generates it's own random response everytime you play.
Enjoy!!
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

print("Rock Paper Scissor Game")
userInput = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors : "))
computerInput = random.randint(0,2)

if userInput > 2 or userInput < 0 :
    print("Invalid Choice!!")
else : 
    print(game[userInput])
    print("Computer Chooses")
    print(game[computerInput])
        
    if userInput == computerInput:
        print("It's a draw!!")
    elif userInput == 0 and computerInput == 2:
        print("You win!")
    elif computerInput == 0 and userInput == 2:
        print("You lose")
    elif computerInput > userInput:
        print("You lose")
    elif userInput > computerInput:
        print("You win!")
