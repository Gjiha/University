# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:39:52 2022

@author: User
"""

def init_list(n,v=lambda x:0):
    
    t=[]
    for i in range(n):
        t += [v(i)]
    
    return t

x0= init_list(10)
print(x0)

x1= init_list(10, v=lambda t: t*2+1)
print(x1)

x2= init_list(10, v=lambda t: ':)'*(t+1))
print(x2)

x3= init_list(10, v=lambda t: (t,)*10)
print(x3)
 