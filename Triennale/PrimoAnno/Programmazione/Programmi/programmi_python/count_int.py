# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:51:01 2022

@author: franc
"""

def count_int(n):
    
    c=0
    
    for i in n:
        
        if type(i)==list:
            c+=count_int(i)
        
        elif type(i)==int:
            c+=1
    
            
    return c
            
        
    
            
    

a=[3, [1,2],5,3]
x=count_int(a)
print(x)
            
            
            