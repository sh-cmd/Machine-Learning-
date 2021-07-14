# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:26:34 2020

@author: shubham
"""

a=input('Enter the sequene of word : ')
a=[i for i in a.split(' ')]
new=set(a)
new=sorted(new)
new1 = " ".join(new)
print(new1)