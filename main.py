import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
'''
        Strings
Strings-a string is a sequence of characters, which can include letters, numbers, symbols, and whitespace
They are enclosed in either single quotes (') or double quotes ("), and can be assigned to variables or used directly in expressions.
Strings are immutable, which means that once a string is created, its contents cannot be changed

'''
name = "Sushant@Kumar 123 *&^"
print(name.upper())  # sab characters uppercase ho jayega
print(name.lower())  # sab characters lowercase ho jayega
print(name.split())  # saare words list ke elements ban jayega in string form
joined_string = " ".join(["this", "is", "a", "sentence"])  # list ko string me change kar dega
print(joined_string)
print(name.find("ant"))  # gives a index value
print(name.replace("@", "_"))
name2 = "sushaNt Kumar"
print(name2.capitalize())  # only capitalize first wird of a string
print(name.count("a"))
print(name2.endswith("mar"))  # gives True of False
print(name2.title())  # capitalize every first character of word
print(name2[0:15])  # slicing
name3 = "   harry Potter   "
print(name3.strip())  # right or left dono side se spaces ko hata dega
print(name3.rstrip())  # right side se spaces ko hata dega
print(name3.lstrip())  # left sode se spaces ko hata dega
print(name3.startswith("harry"))
print(name.swapcase())  # lower se upper and upper se lower
j = " ".join(['123', "23", "Skarn"])  # agar elemnt integer hoga toh error aayega
print(j, type(j))
print("python" + " world")
print("py" * 5)

# # questions - odd or even
# n=int(input("enter a number"))
# if n%2 == 0:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is odd")
# # finding greatest number between two numbers
# n1=float(input("1st No-"))
# n2=float(input("2nd No-"))
# if n1>n2 :
#     print(f"{n1} is greater than {n2}")
# elif n2>n1:
#     print(f"{n2} is greater than {n1}")
# else:
#     print(f"{n1} is equal to {n1}")
#
# # checking palindrome-aage se pichee se same rehta hain
# n=input("Enter The Words")
# s=""
# for i in range(len(n)-1,-1,-1):
#     s=s+n[i]
# if n==s:
#     print(f"{n} is palindrome")
# else:
#     print("not a palindrome")
#
# '''Leap Year'''
# n=int(input("Enter the year-"))
#
# if n%4 == 0 and n%100 !=0 :
#     print("leap year")
# elif n%400==0:
#     print("leap year")
# else:
#     print("not a leap  year")

# loop
# for i in range(1,11):
#     print(i,end=" ")
# print()
# n=int(input("enter first n numbers-"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f"sum of first {n} numbers is-{sum}")
# l=[1,3,4,2,8,9,3]
# sum1=0
# for num in l:
#     if num%2==0:
#         print(num,"Even")
#         sum1+=1
# print("total even numbers in",l,"is", sum1 )
#
s = ""
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

g = 0
for i in range(1, 6):
    for j in range(1, i + 1):
        print(g + j, end=" ", )
    print()
    g += i
