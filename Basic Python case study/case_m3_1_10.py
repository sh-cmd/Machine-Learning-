# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:06:46 2020

@author: shubham
"""
list=[]
a=input('Enter the seqence : ')
b=[i for i in a.split(",")]
list=[i for i in b]
list=sorted(list)
C=','.join(list)
print(C)