# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:52:56 2020

@author: shubham
"""
import csv
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('c:\\users\\shubham\\shubham_learning\\')

dataset = pd.read_csv('BigMartSalesData.csv')
selected_data=dataset.loc[:,['Country','Quantity']]
print(selected_data)
labels_country=np.array(selected_data['Country'])
x_values=np.array(selected_data['Quantity'])
country=np.unique(labels_country)
final_x_values=selected_data.groupby('Country')['Quantity'].count()
print(final_x_values)
# plt.figure(figsize=(40,40))
fig1, ax1 = plt.subplots()
ax1.axis('equal')
plt.pie(final_x_values,labels=country)
#
plt.show()