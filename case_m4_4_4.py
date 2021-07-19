# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:01:59 2020

@author: shubham
"""
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('BigMartSalesData.csv')

data = dataset.loc[:,['Country','Amount']]
print(data)
x = np.array(data['Country'])
z = np.array(data['Amount'])

x1=np.unique(x)
z1 = data.groupby('Country')['Amount'].sum()
print(z1)
new_data=pd.DataFrame(z1)
z2 = new_data['Amount'].values.tolist()
plt.scatter(x1,z2)
plt.xlabel('Country')
plt.ylabel('Amount')
plt.show()