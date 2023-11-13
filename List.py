Juice = ["mango_juice", "Coke", "Apple-juice", "Orange_Juice"]
print(len(Juice))
print(Juice[0], Juice[2])  # 0,2 here is a positive index value
print(Juice[-1], Juice[-3])  # -1,-2 here is a negative index value
print(Juice[0:3])
print(Juice[-1:-4:-1])

for index in range(len(Juice)):
    print(Juice[index])
# Juice[4]="Sugar_cane" Index out of range
print(Juice)

'''List Operations'''
print(Juice * 2)
print(Juice[1:])
print(Juice[0:3:2])
print(Juice[-4:0:2])

'''List Methods Practise'''
# print(dir(Juice))
print(Juice.index("Coke"))
Juice = ["mango_juice", "Coke", "Apple-juice", "Orange_Juice", "Coke"]
print(Juice.index("Coke", 4))
Juice.append(56)  # Takes only one arguments
Juice.append([12, 34])
print(Juice)
Juice.extend([10, 30, 56])  # used to add so many elements in list
print(Juice)
Juice.insert(2, "Pineapple")
print(Juice)
Juice.remove("Coke")
print(Juice)
print(Juice.count("Coke"))

print(Juice.pop(2))
numbers = [10, 20, 45, 12, 31, 98, 8]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
s = numbers.copy()  # if original is  updated then old list is also not updated
print(s)
numbers.clear()
print(numbers)

list1 = [10, 10, 5, 15, 50, 50, 20]
index = list1.index(50)
list1[index] = 5
print(list1)
list1 = [10, 10, 5, 15, 50, 50, 20]
second_index = list1.index(50, index + 1)
list1[second_index] = 5
print(list1)
'''Exercises'''
s = "hello"
b = s.split(" ")
print(b)
c = list(s)
print(c)

custom_list = [1, 2, 3, 4, 5]
for i in range(len(custom_list)):
    custom_list[i] = str(custom_list[i])
s = "|".join(custom_list)
print(s)

'''Nested List'''
day1 = [11, 12, 5, 2]
day2 = [15, 11, 65, 3]
day3 = [10, 56, 43, 8]
day4 = [12, 76, 43, 89]
all_days = [day1, day2, day3, day4]
print(all_days)
print(all_days[0])
print(all_days[0][2])

'''Objects and value'''

x = "apple"
b = "apple"
print(x is b)
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)

'''del ke kaarname'''
s = x
del s[0]  # effect original list also
print(x)


def deletefirst(p_list):
    del p_list[0]
    return p_list


my_list = [1, 2, 3, 4, 5]
print(deletefirst(my_list))
print(my_list)


def delete_first(p_list):
    return p_list[1:]


my_list = [1, 2, 3, 4, 5, 6]
print(delete_first(my_list))
print(my_list)


def custom_insert(p_list, value):
    p_list = p_list + [value]
    return p_list


list1 = [1, 2, 3, 4, 5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)

'''Question
Example

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate(list1, list2)
Output

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''


def concatenate(p_list1, p_list2):
    new_list = []
    for i in p_list1:
        for j in p_list2:
            new_list.append(i + j)
    return new_list


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
x = concatenate(list1, list2)
print(x)
