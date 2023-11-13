import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()+_-={}[]|\:;"
numbers_of_letters = int(input("How many letters do you want in your password? "))
numbers_of_nums = int(input("How many numbers do you want in your password? "))
numbers_of_symbol = int(input("How many symbol do you want in your password? "))
password = ""
for letter in range(1, numbers_of_letters + 1):
    password = password + random.choice(letters)
for number in range(1, numbers_of_nums + 1):
    password = password + random.choice(numbers)
for symbol in range(1, numbers_of_symbol + 1):
    password = password + random.choice(symbols)
print("Your Passwod Can be-", password)
password_list = list(password)
print(password_list)
random.shuffle(password_list)
print(password_list)

advanced_password = ""
for apc in password_list:
    advanced_password = advanced_password + apc
print(f"advanced password is {advanced_password}")
