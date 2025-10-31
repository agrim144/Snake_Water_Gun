# Using numbers for choices:
# 1 → Snake, -1 → Water, 0 → Gun

import random
computer = random.choice([-1, 0, 1])

youstr = (input("Enter your choice: "))
a = youstr.lower()
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0:"Gun" }
you = youDict[a]

# By now we have 2 number (variables), you and number

print(f"You chose {a} and computer chose {reverseDict[computer]}. ")


if(computer == you):
    print("Its a draw")
else:
    if (computer-you) == -1 or (computer-you) == 2:
        print("You lose!")
    else:
        print("You win!")
