# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:30:36 2020

@author: shubham
"""

import numpy as np
a = np.array([np.nan,1,2,3,np.nan,4])
print(a)
print("Remove all non-numeric elements of the said array")
print(a[~np.isnan(a)])