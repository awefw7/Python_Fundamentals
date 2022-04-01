# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:51:16 2022

@author: z2- soft developer
"""

# Task2

myList = [55, "sky", 22.55, b's']

a = myList[0]
b = myList[1]
c = myList[2]
d = myList[3]
a, b = b, a
c, d = d, c
print(a, b, c, d)
