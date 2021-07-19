# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:11:50 2020

@author: shubham
"""

import numpy as np
a = np.array([0,5,4,0,4,4,3,0,0,5,2,1,1,9])
b=[]
c=[]
for i in range(0,10):
    
    if i not in b:
        b.append(i)
#    print(b)
        cnt = list(a).count(i)
        c.append(cnt)
print(c)