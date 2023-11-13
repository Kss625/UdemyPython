import math
import random

print("Welcome To The Game Of Guessing The Number")
Play = input("You Want To Play(Yes/No)-")
if Play == "Yes":
    upper_range = int(input("Enter the Upper Range-"))
    lower_range = int(input("Enter the Lower Range-"))
else:
    print("Thanks For Using The Game")
    quit()

# used for getting number of choices you can also select your own attempts
Random_number = random.randint(lower_range, upper_range)
attempts = round(math.log(upper_range - lower_range, 2))
print(f"   You Have only {attempts} Attempts")
count = 1


def Guessing(R_Number):
    Selected_number = int(input("Guess Your Number-"))
    if Selected_number <= upper_range and Selected_number >= lower_range:
        if Selected_number == R_Number:
            print(f"Congratulations,You Selected Right Number in {count} Attempt")
            quit()
        elif Selected_number > R_Number:
            print("You are far from Answer")

        elif Selected_number < R_Number:
            print(f"You Just nearer to Answer")
    else:
        print("Please Enter Correct Number")


while count <= attempts:
    Guessing(Random_number)
    if count == attempts:
        print("You Have Used all The attempts,Thanks for using Guessing Number Game")
        print(f"The Correct Answer is {Random_number}")
    count = count + 1
