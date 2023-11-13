'''Bill Roulette'''
import random

a = ["sushant", "Mohan", "Ram", "Shyam", "Eddy"]

for i in range(1, 4):
    Random_Choice = random.choice(a)
    print(f"{Random_Choice} have to pay all the Bill of Restaurant")

names = input("Give Everyone's Name,separated by Commas.")
friend = names.split(",")
print(friend)
friend_who_pay = random.choice(friend)
print(f"{friend_who_pay} have to pay all the Bill of Restaurant")
