#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:55:27 2022

@author: fanik
"""
MyName = input ("Enter Name ")
print (MyName)

L = []
L = [123, 'abc', 1.23, {}]
#L.sort()ivan
print(L)
print(L[0])
print(L[2])
print(L[-1])
print(L[-2])
print('*******************')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.pop(2))
print(motorcycles)
print(motorcycles[0])
motorcycles.append('BMW')
print(motorcycles)
print('*******************')
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(motorcycles[0]) # ducati
print(motorcycles[-1]) # BMW
print('*******************')
del motorcycles[0]
print(motorcycles)
print(motorcycles[:2])
print(motorcycles)
print(motorcycles[2:])

motorcycles.sort()
print(motorcycles)

motorcycles.reverse()
print(motorcycles)


print(motorcycles.pop(2))
print(motorcycles)
motorcycles.append('BMW')
print(motorcycles)
print("***********************")
motorcycles.remove('BMW')
print(motorcycles)


del motorcycles[0]
print(motorcycles)
motorcycles.insert(0,'BMW')
print(motorcycles)
motorcycles.insert(1,'honda')
print(motorcycles)
# count element 'honda'
count = motorcycles.count('honda')

# print count
print('The count of honda is:', count)


a = 'the quick brown fox jumps over the lazy dog'

print(a.split())
print(a.find('dog'))

print ("Enter your name:")
x = input()
print ("hi, " + x )


