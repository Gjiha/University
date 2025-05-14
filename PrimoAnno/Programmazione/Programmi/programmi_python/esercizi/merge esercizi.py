# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:05:11 2023

@author: franc
"""
import random as rn
#%%  non ne so il motivo ma questa non funge, ha un qualche problema con i contatori

def merge (l_first, lx, cx, rx):
    
    #scelta delle variabili O(1)
    l_final = []          
    c = 0
    i, j = lx, cx 
    
    while i < cx and j < rx:
       
        if l_first[i] < l_first[j]:           
            l_final.append(l_first[i])
            i += 1
            
        else:           
            l_final.append(l_first[j])
            j += 1
            
        c =+ 1   #contatore cnfronti
        
    if i == cx:
        tx, l_prov, p = rx, l_first, j
    else:
        tx, l_prov, p = cx, l_first, i
    
    while p < tx:
        
        l_final.append(l_prov[p])
        p += 1
    
    for m in range (rx-lx):
        l_first[lx+m] = l_final[m]
        
    return c

def merge_sort(a, lx = 0, rx = None):
    if rx == None:
        rx = len(a)
        
    if rx == lx or rx == lx+1:
        return 0 #affinchè si contino i confronti non si può usare None
    
    cx = (rx+lx)//2
    c0 = merge_sort(a, lx, cx)
    c1 = merge_sort(a, cx, rx)
    c2 = merge(a, lx, cx, rx)   #per portare a galla i confornti bisogna assegnare un valore ad ogni ricorsione 
    
    return c2+c0+c1



#%% funziona!!

def bubble_sort(a, key = lambda x: x, inplace = True ):
    
    if inplace:  #di base crea un alias
        b=a     
    else:
        b=a[:]
    
    ordinata = True
    c = 0 #contatore confronti eseguiti
    
    while ordinata:        
        i, j = 0, 0
        ordinata = False
        
        while i < len(b)-1-j:
            
            c += 1
            if key(b[i]) > key(b[i+1]):  #la funzione lambda key permette di scegliere il criterio del confronto scegliendo una funzione
                
                b[i], b[i+1] = b[i+1], b[i]     #dove avviene lo scambio          
                ordinata = True
                            
            i += 1
            
        j +=1
    return c

#%% 

def test(da = 100, a = 500, step = 100):
    f = open('test liste e merge.csv', 'w')
    for n in range(da, a, step):
        print(n)
        for i in range(100):
            
            L0 = [rn.random() for x in range(n)]
            L1 = L0[:]
            x = bubble_sort(L0)
            y = merge_sort(L1)
        
            f.write( f'{n};{x};{y}\n')
    f.close()

        






















