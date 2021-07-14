# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:40:21 2020

@author: shubham
"""

word=input("Enter the password : ")
let1,let2=0,0
for i in range (0,len(word)):
    letter=ord(word[i])
    if (letter>64 and letter<91):
        let1=let1+1
    elif (letter>96 and letter<123):
        let2=let2+1
        
print('No of Upper case : ',let1)
print('No of lower case : ',let2)
#    print(digit)
#    print(spetial)
    