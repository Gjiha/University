# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:09:06 2023

@author: franc
"""
def hist( a, bins ):
    
    '''
    Input: a una lista di m float e bins una lista di n floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    n = len(bins)+1
    x, c  = 0, 0
    d = [0]*n
    
    for i in bins:
        while c < len(a) and a[c] < i :
            d[x] += 1
            c += 1
        x +=1
    if c != len(a):
        while c < len(a)-1:
            d[n-1] +=1
            c += 1
    return d

a = [1,2,3,4,5,6,7,8,9,10,15,16]
b = [3,6,9,90]
print(hist(a, b))
        
            

            
            
            
    
    

    
        

 

        