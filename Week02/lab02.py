# This is the Python file for the Week 02
# Berhan Erdogan

import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = int(input("Please enter your choice (1=Rock, 2=Paper, 3=Scissors): "))

while playerChoice not in range(1, 4):
    print("Error: Choice must be between 1 and 3")
    playerChoice = int(input("Please enter your choice: (1=Rock, 2=Paper, 3=Scissors)"))

print("Computer is deciding...")
computerChoice = random.randint(1, 3)

playerIndex = choices[playerChoice - 1]
computerIndex = choices[computerChoice - 1]
print("Your Choice:", playerIndex)
print("Computer's Choice:", computerIndex)

if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == 1 and computerChoice == 3:
    print("Rock beats Scissors - You win!")
elif playerChoice == 2 and computerChoice == 1:
    print("Paper beats Rock - You win!")
elif playerChoice == 3 and computerChoice == 2:
    print("Scissors beats Paper - You win!")     
else:
    print("You lose!") 