import random

print("Let's Start The Rolling the Dice")
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


def rolling(dice1, dice2):
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")


rolling(dice1, dice2)


def check_for_rolling():
    try:
        rolling_again = input("Would You Like To Rolling the dice again(Yes/No):")
        return rolling_again
    except (ValueError, TypeError):
        return "Please,Enter Correct Input"


while True:
    output = check_for_rolling()
    if output == "Yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        rolling(dice1, dice2)
    elif output == "No":
        print("Thanks,For using Dice Roller")
        break
    else:
        print("Enter Correct Input either Yes or No")
