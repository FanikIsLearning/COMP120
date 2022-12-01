# -*- coding: utf-8 -*-
"""
Created on Tue Apr 6 15:06:42 2021

@author: Ayesha
"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content! We are learning to read and write into file")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "a")
f.write("\nNow the file has more content added!")
f.close()
print('***********************************')
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.readline())
f.close()
import os
os.remove("demofile2.txt")