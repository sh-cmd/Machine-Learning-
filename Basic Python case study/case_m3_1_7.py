# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:29:06 2019

@author: shubham
"""

fact_no = input('Enter the no:')
fact=int(fact_no)
no=fact
if (no==0):
    print('1')
else:
    for i in range(fact-1):
        no=no-1
        fact=fact*no
    print(fact)
    
