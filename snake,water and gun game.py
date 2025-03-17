# Snake, Water and Gun Game
import random

# Dictionary for mapping choices to numbers
dictyou = {"snake": -1, "water": 0, "gun": 1}

# Get user's choice
you = input("Enter your choice (snake, water, gun): ").lower()

# Validate user input
if you not in dictyou:
    print("Invalid choice! Please enter snake, water, or gun.")
    exit()

# Get computer's random choice
computer_choice = random.choice(["snake", "water", "gun"])
computer = dictyou[computer_choice]

# Convert user choice to number
you = dictyou[you]

print(f"Computer chose: {computer_choice}")

if(computer==-1 or you==0):
    print("you lose")

elif(computer==-1 or you==1):
    print("you win")

elif(computer==-1 or you==-1):
    print("draw")

elif(computer==1 or you==0):
    print("you win")

elif(computer==1 or you==-1):
    print("you lose")

elif(computer==1 or you==1):
    print("draw")

elif(computer==0 or you==-1):
    print("you win")

elif(computer==0 or you==1):
    print("you lose")

elif(computer==0 or you==0):
    print("draw")

else:
    print("something went wrong")