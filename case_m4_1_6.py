# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:49:01 2020

@author: shubham
"""

import numpy as np
import pandas as pd
a = np.arange(0,12)
b=np.reshape(a,(4,3),'c')
print(b)
for i in range(0,4):
    for j in range(0,3):
        if b[i][j]>=5:
            b[i][j]=0
print(b)
            