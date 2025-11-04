# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:23:25 2022

@author: franc
"""

def merge_1( a, b ):
   
    c ,i ,j  = [], 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    
    
    return c 
a = [1, 2, 3, 4, 5, 10, 11, 12, 13]
b = [6, 7, 8, 9]
print(merge_1(a,b))

#%%

def merge (l_first, lx, cx, rx):
    
    #scelta delle variabili O(1)
    l_final = []          
    
    i, j = lx, cx 
    
    while i < cx and j < rx:
       
        if l_first[i] < l_first[j]:           
            l_final.append(l_first[i])
            i += 1
            
        else:           
            l_final.append(l_first[j])
            j += 1
    
    if i == cx:
        tx, l_prov, p = rx, l_first, j
    else:
        tx, l_prov, p = cx, l_first, i
    
    while p < tx:
        
        l_final.append(l_prov[p])
        p += 1
    
    for m in range (rx-lx):
        l_first[lx+m] = l_final[m]
        
    return 

def merge_sort(a, lx, rx):
    if rx == lx or rx == lx+1:
        return
    cx = (rx+lx)//2
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    merge(a, lx, cx, rx)

L = [10, 4, 5, 2, 5, 6, 0, 1, 2, 4, 0, 5, 4, 10]
merge_sort(L, 0, len(L))
print(L)
