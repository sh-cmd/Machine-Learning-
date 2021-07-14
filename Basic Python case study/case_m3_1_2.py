# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:56:56 2020

@author: shubham
"""
data=input('Enter the data : ')
list=[10,15,13,14,64,59,85,55]
list1=sorted(list)
#print(list1)
for i in list1:
    if i==int(data):
        print('data is in the list')
   