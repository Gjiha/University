# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:04:46 2023

@author: franc
"""
'''
Si scriva una funzione, denominata initial_to_substring, che prenda in input una
stringa a e restituisca un dizionario che mappi ogni carattere c di a nella sottostringa più lunga di a che inizi per c.
'''

def initial_to_substring(a):
    
    d = {}
    
    l = []
    
    l = a.split() 
    
    for c in l:
        d[c[0]] = d.get(c[0],'')
        if len(c) > len(d[c[0]]):
            d[c[0]] = c
        
    
    return d


a = 'questo è un mondo Om Oa odio omondibaibaibcibca ma lo aaaaaaaaaaaaa tanto tantissimo p papà uomo éolo'
print(initial_to_substring(a))

#%%


def initial_to_substring(a):
    
    d = {}
    i = 0
    
    
    for c in a:
        d[c] = d.get(c,'')
        if len(d[c]) < len(a[i:]) :
            d[c] = a[i:]
        i += 1
    
    return d


a = 'ciao ciao'
print(initial_to_substring(a))

            
            
        
        


