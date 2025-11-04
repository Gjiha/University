# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:40:03 2022

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
    a= len(n)
    b= len(v)
    Trovato,x,y = False,n,v
     
    if b>a:
        a= len(v)   
        b= len(n)
        y,x = n,v
    p,q=0,0    
    
    while p < (a-b) and Trovato != True:
        if y[q]==x[p+q]:
            q+=1
            Trovato=True
        else:
            p+=1
    if Trovato==False:
        p=-1
    return p

print(find_contains('dolce','dolcemela'))
        
