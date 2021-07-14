# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:04:00 2020

@author: shubham
"""

a=2000
list=[]
#while a<3201:
list=[str(i) for i in range(2000,3201) if(i%5!=0 and i%7==0)]
list1 = ",".join(list)
print (list1)

        