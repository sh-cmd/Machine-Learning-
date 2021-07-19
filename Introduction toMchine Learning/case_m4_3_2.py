# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:16:34 2020

@author: shubham
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('CityTemps.csv')
dataset.columns= ['Year','Month','Moscow','Melbourne','SanFrancisco']
data = dataset.loc[:,['Year','Moscow','SanFrancisco']]
print(data)
y = np.array(data['Year'])
x = np.array(data['SanFrancisco'])
z = np.array(data['Moscow'])

plt.plot(y,x ,'rs',y,z ,'bs')
plt.xlim(2013,2016)
#plt.xticks([0.5,1,1.5,2,3,4])