# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:18:57 2023

@author: franc
"""

a = (1,2,3,4)
b = [10,20,30,40]
c = [100,200,300,400]
print(zip(a,b,c))
for i in zip(a,b,c):
    print(i)
    
    
print(list(zip(a,b,c)))

#%%
def list_sum(a):
    c = 0
    for i in range(len(a)-2):
        if a[i] + a[i+1] == a[i+2]:
            c += 1
    return c

a = [5,3,8,6,14,5]
print(list_sum(a))

#%%




