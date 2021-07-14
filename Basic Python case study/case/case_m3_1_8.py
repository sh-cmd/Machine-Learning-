# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:35:15 2020

@author: shubham
"""
import math 
C=50
H=30
result=[]
list1=[]
D=input('Enter the value of d : ')
list=[D for D in D.split(",")]
list1 = [int(i) for i in list]
i=0
for i in list1:
    S= ((2 * C * i)/H)
    Q= round(math.sqrt(S))
    result.append(Q)

print('output',result)





