'''Love Calculator'''
n = input("Enter Men's Name-")
w = input("Enter men's Name-")
s = n.lower() + w.lower()
t = s.count("t")
r = s.count("r")
u = s.count("u")
e = s.count("e")
l = s.count("l")
o = s.count("o")
v = s.count("v")
e = s.count("e")
add1 = t + r + u + e
add2 = l + o + v + e
s1 = str(add1 + add2)
number = int(s1)
if number < 10 or number > 85:
    print(f"Your Score is {number},You go together like coke and mentos")
elif number >= 40 and number <= 70:
    print(f"Your Score is {number}, you are alright togrther")
else:
    print(f"your Score is {number}")
    print("Think About it")
