print("Hello World")
# quit() used to exit from terminal for python
# three types of errors-syntax error,Logic Errors,RunTime Errors
# Debugging - Correct The Bug From Programmes
# Ways for Debugging--Reading,Running,Ruminating,Retreating
'''computer understand in binary format
source code-->compilers/interpreters--> machine code

'''

# Escape characters
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo Octal value
# \xhh Hex value

# print("Sushant Kumar")#print() is a function in python that gives output written in brackets
print("Sushant\nKumar")  # put a new line
print("Sushant\tKumar")  # put a tab between string
print('Sushant It\'s all Right')  # helps to differentiate between so many same quotes
# print("Sushant \\' Kumar")                    # ek backlash print nhi hoga
# txt=" \rSushant Kumar"                       #cursor ko word ke starting me le aayega
# print(txt)
print("Sk@\bkarn")  # left side wale ko backspace kar dega

'''
TODO- Coding Exercise -1
Print Statement - Python Programming
Write a program with the help of print() statement that prints to the console followings:

My First Program - Print Function
The Print function prints itself like this:
print('output to console')
'''
# Ans Upto 3 lines
print("My First Program - Print Function")
print("The Print function prints itself like this:")
print("print('output to console')")  # output to console me double quotes nhi  lenge kyuki computer confuse ho jayega

# print("""hello
# world
# by sushant kumar
# """)                                 #used to print multiple lines

'''Taking Input From users'''
x = input("What is your Name-")  # Taking String value
print(x, type(x))
y = int(input("Enter Your Age-"))  # Taking integer Input
print(y, type(y))

'''
Exercise-3

Input Function
Write a program that uses input to prompt a user for their name and then prints to the console the number of characters in the inputed name.

Example:

Input : "Elshad" 
Output : 
'''
'''ans upto 2 lines'''
name = input("What is your name? ")
print(len(name))  # len() function is used to find the length of string
print(
    f"your name has {len(name)} Characters")  # new way to print all things in a single or double quote with the help of f-strings

print(len("web2karn@123"))
