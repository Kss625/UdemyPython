''' Functions Calls and Built-in Functions '''
# python Math Module
import math
import random  # randomisaton in python

print(math.pow(25, 2))  # 25**2,
print(pow(25, 2, 3))  # (25**2)%3 ye dusre tarike ka pow function hain jo 3 arguments bhi ke skta hain,ye alag hain
print(math.sqrt(25))  # finding squareroot gives output in float
print(math.pi, math.e)  # math constants
a = 2.4
print("ceil is", math.ceil(a))  # Ceil value means the smallest integral value greater than the number
print("floor is", math.floor(a))  # the floor value means the greatest integral value smaller than the number
print(math.factorial(4))  # use for finding the factorial of number
print(math.gcd(24, 6))  # finding the greatest common divisor
print(math.fabs(10), math.fabs(-10))  # gives absolute value
print(math.exp(4))  # e ki power ke liye istemaal karte hain
print("The value of log 2 with base 3 is : ", end="")
print(math.log(2, 3))

# dusre file se import karne ke liye math ki jagah file ka naam rakh denge

# randomisaton in python
print(random.randint(2, 10))  # generate random integer between given numbers
print(random.random())  # 0 include but 1 is not include
print(random.random() * 5)
l = [10, 20, 45, 3, 4, 67, 98, 100]
print(random.choice(l), random.choices(l))
