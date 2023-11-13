import math


def paint(wall_height, width_height):
    Area = wall_height * width_height
    cans = Area / 4
    print(math.ceil(cans))


paint(2, 5)
'''functions with inputs'''


def Greet(name):  # name is parameter is input given to Greet functions
    print("Hello", name)
    print("How are You?")


Greet("Sushant")  # Sushant is Argument
Greet("Elshad")

'''positional and keyword Arguments'''


def greet_NC(name, city):
    print(f"Hello,{name}")
    print(f"What is weather like in {city}")


greet_NC("Sushant", "Delhi")  # positional arguments
greet_NC(name="Sushant", city="New Delhi")  # keyword arguments


def func():
    result = 1 + 2
    return result


a = func()
print(a)
'''There is a differce between return and print function usage'''


def format_name(f_name, l_name):
    """This function formats first and last name"""
    if f_name == "" or l_name == "":
        return "name or last name cannot be empty"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name},{formated_l_name}"


format_name("sk", "karn")
a = format_name("elshad eddy", "karimov")
print(a)
'''Mini-Calculator'''


def opera_tion(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return


num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
operation = input("Pick operation from this list (+,-,*,/)")
output = opera_tion(num1, num2, operation)
print(f"{num1} {operation} {num2} = {output}")
n3 = int(input("Enter the third number "))
new_output = opera_tion(n3, output, operation)
print(f"{n3} {operation} {output} = {new_output}")
