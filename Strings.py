my_name = "Sushant Kumar"
print(my_name[0], my_name[1], my_name[5])
print(my_name[2:8], my_name[:], my_name[:9], my_name[1:])
print(my_name[2:15:2])
print(my_name[-16:])
print(len(my_name))

'''sum of digits of numbers'''
# def sum_of_digits(n):
#     s=str(n)
#     sum=0
#     for i in s:
#         sum=sum+int(i)
#     return sum
# n=int(input("Enter Your number-"))
# print(f"Sum of digit of Given Numbers {n} is: {sum_of_digits(n)}")


'''Strings Traversal'''
# fruit="banana"
# for i in range(0,len(fruit)):
#     print(fruit[i],end=" ")
# print()
# i=0
# while i<len(fruit):
#     print(fruit[i],end=" ")
#     i=i+1
# print()
# '''Backward Traversal'''
# for j in range(len(fruit)-1,-1,-1):
#     print(fruit[j],end=" ")
# print()
# n=input("Enter a string: ")
# i=len(n)-1
# while i>=0:
#     print(n[i],end=" ")
#     i=i-1
# print()

'''String Operations'''
# print("sushant"+"karn",)
# print("skarn"*5)
# print("a" in "skarn")

'''String Methods'''
my_name = "     Elshad Karimov udemy"
print(type(my_name))
print(dir(my_name))
help(str.capitalize)
print(my_name.capitalize())
print(my_name.count("a"))
print(my_name.title())
print(my_name.lower())
print(my_name.upper())
print(my_name.index("a"))
print(my_name.startswith("Els"))  # Gives True if String Startswith Els
print(my_name.lstrip())  # remove spaces in left side
print(my_name.find("had"))
print(my_name.find(" ", 16))
print(my_name.split())
print(my_name.split(" "))
print(my_name.replace("had", "mko"))
a = my_name.split()
s = " ".join(a)
print(s)

'''escape sequence'''
question = '''He said "what's your name?'''
print(question)
question = 'He said "what\'s your name?'
print(question)
'''string formatting'''
error_no = 23784568
name = "edy"
print("hello, %s" % name)
print("%x" % error_no)
print('Hey %s, there is a 0x%x error' % (name, error_no))
print('Hello, {}'.format(name))
print('Hey {}, there is a0x{:x} error!'.format(name, error_no))
print(f'Hey {name}, there is a0x{error_no:x} error!'.format(error_no=error_no, name=name))
print(f"Hey {name}, there is a {error_no:#x} error!")
print()
'''printing pattern'''


def print_pattern(n):
    s = "*"
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(s, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(i, 0, -1):
            print(s, end=" ")
        print()


print_pattern(6)
