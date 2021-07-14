# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:33:29 2020

@author: shubham
"""

items = []
a=input('Enter the binary numbers : ')
list = [i for i in a.split(',')]
for p in list:
    x = int(p, 2)
    if x!=x%5:
        items.append(p)
print(','.join(items))