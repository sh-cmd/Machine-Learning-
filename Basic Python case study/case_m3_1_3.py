# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:26:37 2020

@author: shubham
"""

import time
t = time.localtime()
if t.tm_hour < 7 and t.tm_hour>18:
    print ('It is a night')
else:
    print ('It is night')
#print(localtime)