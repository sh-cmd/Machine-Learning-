# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:04:18 2020

@author: shubham
"""

import os 
import numpy as np
import pandas as pd
os.chdir('c:\\users\\shubham\\shubham_learning\\')

data = pd.read_csv('SalaryGender.csv')

#print(data)
men_with_phd= data[(data['Gender']==1) & (data['PhD']==1)]
#print(men_with_phd)
print('No of men with PhD : ',len(men_with_phd))
women_with_phd= data[(data['Gender']==0) & (data['PhD']==1)]
#print(women_with_phd)
print('No of women with PhD : ',len(women_with_phd))
age_PhD = data[['Age','PhD']]
Age_with_PhD = age_PhD[(age_PhD['PhD']==1)]
#print(Age_with_PhD)
print('tatal no of peaple with PhD : ',len(Age_with_PhD))