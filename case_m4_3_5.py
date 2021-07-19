# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:52:06 2020

@author: shubham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df)
#sns.lmplot(size = 'age', x='preTestScore',y='postTestScore',data=df)
#sns.lmplot(size = 300, x='preTestScore',y='postTestScore',data=df)
plt.scatter(df.preTestScore, df.postTestScore, s=df.age)
plt.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)
