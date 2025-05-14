# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:18:04 2022

@author: franc
"""

def bin_search(k, bins):
    
    '''
    prende in imput un int o float e una lista
    la funzione dà in imput la posizione che l'int occuperebbe all'interno della lista

    '''
    
    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    
    
    lx, rx = 0, n
    trovato = False
    
    while not trovato:
        
        cx = (lx+rx)//2
        
        if k >= bins[cx-1]  and k < bins[cx]:
            trovato = True
            
        elif k < bins[cx-1]:
            rx = cx-1
            
        else:
            lx = cx+1
            
    return cx
        

print(bin_search(10,[6,8,12,23]))