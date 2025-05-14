# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:20:20 2022

@author: franc
"""

def dizionario_1(a):
    
    d = {} #{'0':0}                #O(1)
    #x=a[0]
    #d={ x[0] : [ a[0] ] }
    #f=a[1:]
    
    for c in a:                  #O(n)
    
        if c=='':                #O(1)
            continue
        
        if not c[0] in d:        #O(1)
            d[c[0]] = [c]          #creare la lista(O(1))+scrittura nel dizionario(O(1))
            
        elif c[0] in d:          #O(1)
            d[c[0]].append(c)    #lettura(O(1))+append(O(1))
            
    return d #costo totale n*O(1)=n

print( dizionario_1(['mario','mamma','nonno','genny','nonna']))

print( dizionario_1(['mario','','mamma','nonno','genny','nonna']))


        
#%%
import os

def dizionario_2(f):
    
    d = {}
    mappa_punti_valori={6:0.3, 7:0.4, 8:0.6, 9:1, 10:1.5}
    cartella=os.listdir(f)
    
    for x in cartella:
        
        if x.split('.')[-1] == 'txt':
            
            path=os.path.join(f,x)
            o=open(path)
           
            for line in o:
                
                if line == '\n':
                    continue
                
                t,y=line.split(';')
                y=int(y)
                
             
                d[t] = d.get(t, 0) + mappa_punti_valori.get(y, 0)
              
            o.close()
 
    return d
                    
print(dizionario_2("cartella_per_es_dizio"))




    
                    

                
                
                
                
                
                
        