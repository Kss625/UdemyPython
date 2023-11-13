print(type(None), type(True), type(False))
# if-else Statement
print("Welcome To Mortgage Calculator ")
salary = int(input("What is your Salary? "))
if salary >= 2000:
    print("Eligible For Mortgage")
else:
    print("You Are Not Eligible For Mortgage")
    # pass condition just helps to skipping the part of block

# nested if - else  conditional
x = 4
y = 6
if x == y:
    print("x is equal to y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("y is greater than x")

if salary >= 2000:
    print("Eligible For Mortgage")
    credit = int(input("Enter Your Credit Score"))
    if credit > 800:
        print("Interest Rate is 4%")
    else:
        if credit > 600:
            print("Interest Rate is 6%")
        else:
            print("Interest Rate is 8%")
else:
    print("You Are Not Eligible For Mortgage")

'''Exercise 5-
Even or Odd
Write a program that takes an integer number from console and checks whether if a number is an odd or even.

Example:

Input : 100
Output : Even
Hint:

Use modulus operator that we have learnt in previous section

IMPORTANT! - To pass the coding exercises test

Prompt for input must be (space at the end) : Enter a number:

Print statements must be Even or Odd
'''

'''Answer Upto 5 lines below'''
number = int(input("Enter integer number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

'''

Body Mass Index (BMI) Calculator
Write a program that calculates  the Body Mass Index (BMI) based on a user's weight and height and interprets it based BMI graph below.



It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight

Over 18.5 but below 25 their weight is normal

Over 25 but below 30 they are overweight

Over 30 but below 35 they are obese
'''
'''Answer Upto 14 Lines'''
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# TODO
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Your bmi is", round(bmi, 2), end=", ")
    print("your weight is normal.")
elif bmi >= 25 and bmi <= 30:
    print("Your bmi is,", round(bmi, 2), end=", ")
    print("overweight")
else:
    print("Your bmi is,", round(bmi, 2), end=", ")
    print("Obese")

'''Exercise-7
Burger order
Write a program that calculates final bill Burger Order Price based on a user's choice.

Price List.

Mini Burger (M) : $5

Normal Burger (N): $8

Large Burger (L) : $10

Add Mushroom : For Mini and Normal = $1, For Large = $2

Extra Cheese : $1



Example Input

size = "N"
add_mushroom = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $9.
'''
# TODO
size = input("What size Burger do you want? M,N or L ")
add_mushroom = input("Do you want mushroom? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if size == "M":
    price = price + 5
elif size == "N":
    price = price + 8
elif size == "L":
    price = price + 10
else:
    print("Enter valid Input")
if add_mushroom == "Y":
    if size == "M" and size == "N":
        price = price + 1
    else:
        price = price + 2
else:
    price = price + 0
if extra_cheese == "Y":
    price = price + 1
else:
    price = price + 0
print("Your final bill is: " + "$" + str(price) + ".")
#let's learn something
