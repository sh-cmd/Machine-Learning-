# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:41:39 2020

@author: shubham
"""

import numpy as np
a = np.random.random((3,3))
print("Original array:")
print(a)
a[[1, 2]] = a[[2, 1]]

print(a)