# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:37:39 2020

@author: shubham
"""

from numpy.linalg import matrix_rank
#a = np.random.random((3,3))
#raw1=[1,2,4,4]
#raw2=[3,4,8,0]
#a = np.array([raw1,raw2])
#a=np.array([1,1,1,1])
a=[[1,2,3],[2,3,5],[3,4,7],[4,5,9]]
print(a)
print(matrix_rank(a)) # Full rank matrix

#I=a; I[-1,-1] = 0. # rank deficient matrix
#print(matrix_rank(I))
#
#print(matrix_rank(np.ones((4,)))) # 1 dimension - rank 1 unless all 0
#
#print(matrix_rank(np.zeros((4,))))