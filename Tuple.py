# declaring a Tuple
# a=tuple()
# print(a,type(a))
# b=(1)# not a tuple as , is not given
# print(1,type(b))
# c=(1,)
# print(c,type(c))
#
# x=10,20
# print(x,type(x))
#
# country=("India","America","Sri-lanka")
# print(country[2])
# print(country[0:3])

# country[2]="nepal" not allowed as Tuple is immuatable


# tuple to list
# country_copy=list(country)
# print(country_copy)

'''Unpacking Tuples'''
a = b = c = d = 10
print(a, b, c, d)
x, y, z = 10, 20, 30
print(x, y, z)
# list me bhi aisa hota hain

my_tuple = ("one", "two", "three", "four", "five", "six")
for i in my_tuple:
    print(i)
print()
for i in range(len(my_tuple)):
    print(i, my_tuple[i])
print()
'''new way '''
for index, value in enumerate(my_tuple, 0):  # by default 0
    print(index, value)
