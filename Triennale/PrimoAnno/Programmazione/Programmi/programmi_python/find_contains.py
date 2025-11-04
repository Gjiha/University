# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:47:08 2022

@author: User
"""

def find_contains(n,v):
    '''
    
    Parameters
    ----------
    n : inserire una stringa

    Returns: numero di vocali
    -------
    None.

    '''
    
    x,y=n,v
    p,q=0,len(y)
    
    if len(n)<len(y):
        y,x=n,v
        q=len(y)
    
        
    while p< len(x)-len(y):
        
        x1=x[p:p+q]
        
        if y==x1:
            break
        else:
            p+= 1
    return p
        

print(find_contains('dolce','adolcemario'))
