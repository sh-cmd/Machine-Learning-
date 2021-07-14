# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:45:27 2020

@author: shubham
"""
correct_pin=123456
Total_money=10000
PIN=input('Enter ATM or CARD PIN to proceed:')
if int(PIN)==correct_pin:
    print('Welcome to shubham bank')
    opt=input('Enter your option 1 for Case withdrawal 2 for Cash credit 3 for Change pin : ')
    if int(opt)==1:
        a=input('Enter the Required money : ')
        Total_money=Total_money-int(a)
    elif int(opt)==2:
        a=input('Enter the credit money : ')
        Total_money=Total_money+int(a)
    elif int(opt)==3:
        a=input('Enter the new PIN : ')
        correct_pin=int(a)
    else:
        print('invalid pin : ')
else:
    print('invalide pin')