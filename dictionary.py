'''In Dictionary Data Organises In Key-Value Pair '''
# a={"name ":"Sushant",
#    "Age":19,
#    "Month Of Date Of Birth":"August"
#    }
# print(a)
# print(a.keys())
# print(a["Age"]) # we don't use index value,use keys to acces their values
#
# a["Age"] = 20 # update the current dictionary
# print(a)
# a["Roll_No"]=14 # if key is not present then a new key is added in dictionary
# print(a)
'''Traverse and search of elements'''
# for i in a:# traversing
#     print(f"{i}:{a[i]}")
# for i in a:
#     if i=="Age":
#         print("It Exists In Dictionary")
#         print(i,a[i])

'''Remove Elements from Dictionary'''
# a.pop("Roll_No") # remove key-value pairs from dictionary
# print(a)
# result=a.pop("Age")# result takes value of given key and remove the element from dictionary
# print(a)
# result1=a.popitem()#remove last key-value pair from dictionary and store both key and pair
# print(result1,a)
# a["Age1"]=34
# del a["Age1"]# doesn't store values
# print(a)
# a.clear()# delete all the key-value pairs from dictionary
# print(a)

'''In/Not in operator'''
# profile={"name":"Sushant karn","Age":"19","Class":"B.Tech(ME)"}
# print("name" in profile)# True,only checks key not values
# print("height" not in profile)# True


'''Nested-Dictionary'''
# programming_language={
#     "Elshad":"Python",
#     "sushant":"java",
#     "Edy": {"java":5, "Python":10, "C#":3}
# }
# print(programming_language["Edy"]["Python"])

'''Adding a New Dictionary To A List'''
# programming_language = [
#     {"user_name": "Elshad",
#      "favorite_languages": ["Python", "Java", "C#"],
#      "experience": 10
#      },
#     {"user_name": "Renad",
#      "favorite_languages": ["Scratch", "Python"],
#      "experience": 2
#      },
# ]
# def add_new_user(a,b,c):
# # another way new_dictionary={} and new_dictionary["username"]
#     new_dictionary={
#         "user_name": a,
#         "favorite_languages": b,
#         "experience": c,
#     }
#     programming_language.append(new_dictionary)
#     return programming_language
#
# print(add_new_user("Edy",["Java","Kotlin","Swift"],10))

'''Handling Missing key in dictionary'''
# items={
#     "Chips":10,
#     "Kurkure":24,
#     "maggi":23
# }
# #print(items["momos"]) gives error as momos key not exist in given dictionary
# quantity=items.get("Chips")#methods for existing key in given dictionary
# print(f"Number of Chips Packet is {quantity}")
# quantity2=items.get("Momos","The items does not exist")#methods for not existing key in given dictionary
# print(f"Number of Momos in packet is {quantity2}")# if The items does not exists not given then None is print
# print(items)
# quantity3=items.setdefault("pasta","Not Tasty")# default None lega
# print(items)#setdefaulty elements ko set kar dega

'''Keys In Dictionary'''

# custom_dict={
#     0:"Zero",
#     1:"One",
#     2:"Two",
#     3:"Three",
#     4:"Four",
#     5:"Five"
# }
# device_list=["Phone","laptop","tablet","Tv"]
# new_dict={}.fromkeys(device_list)
# print(new_dict)
# new_dict={}.fromkeys(device_list,0)
# print(new_dict)
# keys = custom_dict.keys()
# print(keys)


'''checking given elements is a string or integer'''
# def group_types(p_list):
#     new_dict={}.fromkeys(p_list)
#     for i in new_dict:
#         if isinstance(i,int):
#             new_dict[i]="Integer"
#         elif isinstance(i,str):
#             new_dict[i]="String"
#     return new_dict
# custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
# print(group_types(custom_list))
'''Items Method'''
# custom_dict={
#     0:"Zero",
#     1:"One",
#     2:"Two",
#     3:"Three",
#     4:"Four",
#     5:"Five"
# }
# print(custom_dict.items())
# for key,items in custom_dict.items():# efficient method nowadays
#     print(key,items)
# print()
# for items in custom_dict.items():
#     print(items)
'''A Good problem '''
# def value_length(p_dict):
#     tuple_dict = p_dict.items()
#     final_dict={}
#     for key in p_dict:
#             final_dict[key]={p_dict[key]: len(p_dict[key])}
#     return final_dict

# names_dict = {
#     1 : "Elshad",
#     2 : "Renad",
#     3 : "Johanna",
#     4 : "Appmillers"
# }
# Another Solution
# def value_length(p_list):
#     output_dict={}
#     for key,value in p_list.items():
#         # print(key,value)
#         output_dict[key]={}
#         output_dict[key][value]=len(value)
#     return output_dict
# print(value_length(names_dict))


'''Update method'''
# custom_dict={
#     0:"Zero",
#     1:"One",
#     2:"Two",
#     3:"Three",
#     4:"Four",
#     5:"Five"
# }
# custom_dict2={
#     8 : "Eight",
#     9 : "Nine",
#     1 : "New_One",#order is preserve but new value is added with new key
#     2 : "New_Two"
# }
# custom_dict.update(custom_dict2)
# print(custom_dict)


'''Concatenate three dictionary'''
# dict1={1: "one", 2: "two"}
# dict2={3: "three", 4: "four"}
# dict3={5: "five", 6: "six"}
#
# def concatenate(a,b,c):
#     a.update(b)
#     a.update(c)
#     return a
# print(concatenate(dict1,dict2,dict3))

'''values method in dictionary'''
# custom_dict={
#     0:"Zero",
#     1:"One",
#     2:"Two",
#     3:"Three",
#     4:"Four",
#     5:"Five"
# }
# keys=list(custom_dict.keys())
# values=list(custom_dict.values())
# print(keys)
# print(values)
# print("Five" in values)
# print(values.index("Four"))

'''Removing Empty Items'''
# custom_dict = {
#     "name" : "Elshad",
#     "age" : 28,
#     "city" : None
# }
#
# def remove_empty_items(p_dict):
#     output_dict={}
#     for key in p_dict:
#         if p_dict[key]==None:
#             break
#         else:
#             output_dict[key]=p_dict[key]
#     return output_dict
# print(remove_empty_items(custom_dict))

'''copy method'''
# person = {
#     "name" : "Elshad",
#     "age" : 28,
#     "city" : "London"
# }
# new_person = person#both of them hava same  refrence
# person["city"] = "NewYork"
# print(person,new_person)
# #to end this connfusion
# person1 = {
#     "name" : "elshad",
#     "age" : 28,
#     "city" : "London"
# }
# new_person1=person1.copy()#not affect new dictionary
# person1["city"]="Brazil"
# new_person1.update({"roll_no":13})
# print(person1,new_person1)

'''Deep Copy'''
# import copy
# city_list = ["london","berlin","paris"]
# language_list = ["English","German","French"]
# name_list = ["Edy","John","Ewan"]
# person = {
#     "name" : name_list,
#     "city" : city_list,
#     "language" : language_list
# }
# new_person1=person.copy()
# new_person1["city"].append("Delhi")
# print(new_person1)
# print(person)
# new_person = copy.deepcopy(person)
# new_person["city"].append("Madrid")
# print(new_person["city"])
# print(person["city"])
'''dictionary operations'''
custom_dict = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}
print("Zero" in custom_dict.values())
print(1 in custom_dict.keys())
print(len(custom_dict))
print(all(custom_dict))  # key 0 nhi hona chahiye
print(any(custom_dict))  # koi bhi key true hona chahiye
print(sorted(custom_dict))  # ascending order me key ko arrange karna chahiye

# b=dict({"name":"Sushant"})or {"name":"Sushant"}
# print(b)
