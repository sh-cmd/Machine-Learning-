# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:03:31 2020

@author: shubham
"""

import numpy as np
import pandas as pd
a = np.arange(0,11)
#m = (a > 2) & (a < 9)
#a[m] *= -1
#print(a)
for i in a:
    if i>2 and i<9:
        a[i]*=-1
print(a)