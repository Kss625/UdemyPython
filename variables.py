# variable is a name that refers to value.It store this value..
# we use = for this
'''
1.variable should not start with numbers and special characters except _
2.reserved keywords are not used as a variable
3.special characters not allowed in python even after first characters is letter except _,but integers allowed after first characters

'''
# edy = 1234567
# print(edy)
# n="I am learning Python"
# print(n)
# n=17#assigning a new value to variable
# print(n)


'''
Exercise 2-Switch values
Write a program that switches the values stored in the variables a and b

a = 10
b = 20
Output

a=
20
b=
10

answer is upto 32 to 40 lines 

'''
a = 10
b = 20
t = a + b
a = t - b
b = t - a
print("a=")
print(a)
print("b=")
print(b)

'''Exercise 4-

Data Types - Weeks in Years
Write a program that converts number of years to the weeks. if the input was 2, then the output should be 2 * 52 = 104, because we have 52 weeks in 1 year.

Example Input

2
Example Output

2 * 52 = 104

There are 104 weeks in 2 years


Hint:

The prompt for input function has to be as shown below, otherwise the test case will not work.

'Enter number of years'
'''
# Ans is upto 3 lines below
years = int(input("Enter number of years "))
weeks = years * 52
'''fString and rounding numbers'''
print(f"There are {weeks} weeks in {years} years")

# Round
print(10 / 3)
print(round(10 / 3))
print(round(3.3345555, 5))  # 5 means kitne place tak round karna hain
