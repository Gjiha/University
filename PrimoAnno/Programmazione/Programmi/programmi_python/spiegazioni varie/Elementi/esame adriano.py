# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:59:51 2023

@author: franc
"""

d1= {'k0':6, 'k1':'python',6:3.14 }

d0= {'k0':6, 'k':'python',6:3.14 }

x = d1.keys()
y= d0.keys()
l=[]

for c in x:
    if c in y:
        l.append(c)
        
print(l)

#%%

def intersection(d1, d2):
    lista = []
    
    for key in d1:
        if key in d2:
            lista.append(key)
    return lista

d1= {'k0':6, 'k1':'python',6:3.14 }

d0= {'k0':6, 'k':'python',6:3.14 }

print(intersection(d1, d0))