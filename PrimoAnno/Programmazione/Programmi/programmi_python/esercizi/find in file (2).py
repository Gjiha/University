# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:43:56 2023

@author: franc
"""

#%% solo riga
def find_in_file( filename, k):
    
    c, i = [], 1 
    
    file = open(filename)
    for line in file:  #O(n)      
        if k in line:  #O(m)
            c.append(i)
        i += 1         #O(1)
        
    file.close()
    
    return c

print (find_in_file('bins(hist).py', 'len'))

#%%

def find_in_file_2( filename, k) :
    c, i, x = [], 1, 0
    
    file = open(filename)
    
    for line in file:
        for x in range(len(line)-len(k)):
            if line[x:x+len(k)] == k:
                c.append((i, x))
                
        i += 1
    file.close()
    
    return c

print (find_in_file_2('Merge.py', 'len'))
    
            

