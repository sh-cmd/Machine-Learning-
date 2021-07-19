# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:44:52 2020

@author: shubham
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('Hurricanes.csv')
print (dataset)

x = np.array(dataset['Year'])
z = np.array(dataset['Hurricanes'])
z2 = dataset['Hurricanes'].values.tolist()
x2 = dataset['Year'].values.tolist()

print (z2)
print (x2)

# plt.plot(x_axis_year,y_axis_hurricanes)
plt.xlabel('Year')
plt.ylabel('The number of hurricanes')
# plt.show()
plt.bar(x,z)
#plt.bar(x2,z2)
plt.show()