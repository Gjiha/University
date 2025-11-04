# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:07:54 2022

@author: User
"""

def remove_none(n):
    '''
    prende in imput una lista e ne elimina l'elemento None

    '''
    
    i = 0
    
    while i < len(n) :
        
        if n[i] == None:
            del(n[i])
            i += 1
            
        else:
            i += 1
    return n

a = [5,7,(None),'mario',(0,4),True]
x0 = remove_none(a)
print(x0)

