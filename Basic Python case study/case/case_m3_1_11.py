# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:18:36 2020

@author: shubham
"""
list1=[]
a=input('Enter the sequence: ')
list=[i for i in a.split(',')]
for i in list:
    list1.append(i.upper())
list2=''.join(list1)
print(list2)