# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:45:31 2020

@author: shubham
"""

import csv
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('c:\\users\\shubham\\shubham_learning\\')

dataset = pd.read_csv('BigMartSalesData.csv')
#print(dataset.head())
selected_data=dataset.loc[:,['Month','Quantity']]
x=np.array(selected_data["Month"])
y=np.array(selected_data["Quantity"])
#print(x,y)
x2=np.unique(x)
print(x2)
y2=selected_data.groupby('Month')['Quantity'].count()
#print(y2)
df=pd.DataFrame(y2)
#print(df)
y3=df['Quantity'].values.tolist()
print(y3)
plt.bar(x2,y3)
plt.xlabel('Month of Sales')
plt.ylabel('Total Quantity Sales')
plt.grid()
plt.show()
