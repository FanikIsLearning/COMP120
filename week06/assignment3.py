#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:27:00 2022

@author: fanik
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#ex1.1
print("""apple, 
orange, 
pineapple""" )
print("----------------")

#ex1.2
firstname = "HOI KIT"
lastname = "FAN"
address = "1123 ABC STREET,MISSISSAUGA"
full_list = f"I am {firstname} {lastname}, living in {address}"
print(full_list)
print("----------------")

agile = ["scrum", "xp", "kanban"]
print(agile)
print(agile.pop(2))
print(agile)
agile.insert(2,"Devop")
print (agile)
agile.append("kanban")
print(agile)
print(agile[-1:-2:-1])
print("----------------")

ex3 = ["comp100","comp120","comp213"]
print(f"you are enrolled in {ex3[0]}")
print(f"you are enrolled in {ex3[1]}")
print(f"you are enrolled in {ex3[2]}")

ex3.append("gnet129")
print(f"you are enrolled in {ex3[0]}, {ex3[1]}, {ex3[2]}, and {ex3[3]}")

print("----------------")

#ex4
favorite_languages = {
    'jen': 'HTML',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'C#',
    }

favorite_languages['phil'] = 'Python'
favorite_languages['ivan'] = 'OMG'
del favorite_languages['ivan']
for x in favorite_languages.values():
    print(x)

print("----------------")
#ex5
student = {
    'student name': 'ivan',
    'age': '29',
    'semester': '1',
    'grade': 'gg',
    }
for five_keys in student.keys():
    #print(f"{five_keys}", end=",  ", flush=True)
    print(f"{five_keys}")
    
print("----------------")
for five_values in student.values():
    #print(f"{five_values}", end=",  ", flush=True)
    print(five_values)
    
print("----------------")
#ex6
temperature = float(input('Enter a temperature: '))
if temperature < 98:
    print ("cold")
elif temperature > 98:
    print ("hot")
else:
    print ("normal")
print("----------------")
#ex7
agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ','Responding to change']
for i in agile_values:
    print(i)
print("----------------")
#ex8
def team_collaboration():
    team_software = input('Enter a software: ')
    print (f"I use {team_software} software for team collaboration ")
team_collaboration()
print("----------------")
#ex9
project_id="123" 
def project(): 
    project_id="9090"
    print(f"My internal project id is: {project_id}")
print(f"My global project id is: {project_id}")

project()
print("----------------")
#ex10
import calendar
yy = 2021
mm = 10
print(calendar.month(yy,mm))
print("----------------")
#ex11
import math

print(math.sqrt(5))
print(math.sin(3))
print(math.tan(3))
print(math.cos(3))
print(math.log2(10))
print("----------------")
#ex12