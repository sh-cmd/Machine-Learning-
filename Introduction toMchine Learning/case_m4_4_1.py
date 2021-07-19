# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:38:41 2020

@author: shubham
"""

#Plot Total Sales Per Month for Year 2011.  How the total sales have increased over months in Year 2011. Which month has lowest Sales?
import csv
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('c:\\users\\shubham\\shubham_learning\\')

dataset = pd.read_csv('BigMartSalesData.csv')
print(dataset.head())
selected_data=dataset.loc[:,['Month','Quantity']]
x=np.array(selected_data['Month'])
y=np.array(selected_data['Quantity'])
plt.plot(x,y)
plt.xlabel('Month of Sales')
plt.ylabel('Total Sales')
plt.grid()

plt.show()
