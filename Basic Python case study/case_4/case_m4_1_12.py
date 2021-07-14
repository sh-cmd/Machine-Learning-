# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:20:17 2020

@author: shubham
"""
import numpy as np
a = np.arange(0,60).reshape(2,3,5,2)
print(a)
print(a.sum(axis=2) , a.sum(axis=3))
p