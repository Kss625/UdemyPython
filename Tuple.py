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
# a = b = c = d = 10
# print(a, b, c, d)
# x, y, z = 10, 20, 30
# print(x, y, z)
# # list me bhi aisa hota hain
#
# my_tuple = ("one", "two", "three", "four", "five", "six")
# for i in my_tuple:
#     print(i)
# print()
# for i in range(len(my_tuple)):
#     print(i, my_tuple[i])
# print()
# '''new way '''
# for index, value in enumerate(my_tuple):  # by default 0
#     print(index, value)


'''
Even Index with Enumerate
Implement a function which takes as a parameter a tuple and return a new tuple but only have even index elements from original tuple.

Hint : Use enumerate() function
'''

# def even_index_items(p_tuple):
#     # TODO
#     new_tuple = tuple()
#     for index, value in enumerate(p_tuple):
#         if index % 2 == 0:
#             new_tuple = new_tuple + tuple(p_tuple[index])
#
#     return new_tuple
#
#
# my_tuple = ("a", "b", "c", "d", "e", "f", "g")
# print(even_index_items(my_tuple))


'''Searching Elements in Tuple'''
# My_Tuple = (1,2,3,4,5,6,7,8)
#
# def search_elements(p_tuple,p_items):
#     for index,value in enumerate(p_tuple):
#         if value==p_items:
#             return index
#     return "Item Does Not Exist"
# item=int(input("Enter Item To Search In Tuple: "))
# print(search_elements(My_Tuple,)

'''Tuple Operations'''
t1 = (1, 2, 3)
t2 = (4, 5, 6)

result1 = t1 + t2  # Addition Operators
print(result1)
result2 = t1 * 3  # multiplication operators
print(result2)
print(1 in t1)  # logical operators
print(t1[0:3])  # slicing in python
print(t1[-3:])
test = (1, 4, 3, 0, 3, 5, 7, 1, 1, 1)
''' Some tuple Functions'''
print(test.count(1))
print(test.index(5))
print(max(test), min(test))

list = ["skarn", "Coders", "Sushant"]
list_tuple = tuple(list)
print(list_tuple, type(list_tuple))


def most_frequent(p_tuple):
    max_count = 0
    item = p_tuple[0]
    for value in p_tuple:
        current_item_count = p_tuple.count(value)
        if current_item_count > max_count:
            max_count = current_item_count + max_count
            item = value
    return (item, max_count)


my_tuple = ("a", "b", "c", "d", "e", "a", "b", "b", "c")
print(most_frequent(my_tuple))




'''nested tuples'''
fruit = [("mango", "Apple", "banana", "strawberry"), ("Delhi", "Mumbai", "kolkatta", "Mumbai")]

for inf in fruit:
    # print(f"Fruit : {inf[0]},City : {inf[1]},")
    print("Fruit : {} City :  {}".format(inf[0], inf[1]))  # format string

print("1+2={} and 4+5={}".format(3, 5))
