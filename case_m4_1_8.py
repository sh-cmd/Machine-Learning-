# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:44:24 2020

@author: shubham
"""

import numpy as np
import pandas as pd
b = np.random.random((10,10))
print(b)
max_val,min_val=b.max(),b.min()
print('max value is %f and min value is %f' % (max_val,min_val))