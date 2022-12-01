# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:59:19 2021

@author: Centennial
"""
empty_dict = {}
# Here is a prefilled dictionary

filled_dict = {"one": 1, "two": 2, "three": 3, "three": 3}
filled_dict1 = {'one': 1, 'two': 2, 'three': 3, 'Three': 3}
print(filled_dict1)
print(filled_dict) #{'one': 1, 'two': 2, 'three': 3}
x=filled_dict["three"]
print(x)
print("***************************")
print(filled_dict)
k = filled_dict.keys()
v=filled_dict.values()
print(k) #dict_keys(['"one": 1, "two": 2, "three": 3])
print(v) #dict_values([1,2,3])
# change values
filled_dict["one"] = 100

print(filled_dict) # {"one": 100, "two": 2, "three": 3}
print("*********************")
print(filled_dict.get("two"))
# Adding items
filled_dict["four"] = 4
print(filled_dict) # {"one": 100, "two": 2, "three": 3,"four":4}

#Removing Items
#The pop() method removes the item with the specified key name:
filled_dict.pop("three")
print(filled_dict) #{"one": 100, "two": 2, "four":4}

#Looping Through a Dictionary’s Keys in a Particular Order
for x in filled_dict:
print(filled_dict[x]) # 100,2,4