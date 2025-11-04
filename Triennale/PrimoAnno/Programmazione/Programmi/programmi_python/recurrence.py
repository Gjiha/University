# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:52:35 2022

@author: User
"""

def recurrence (n,v):
    
    q,c,m,m_f=0,0,0,0
    
    
    for p in v:

        for i in n:
        
            if i==p:
                m=i
                c+=1
               
        if c>q:
            q=c
            c=0
            m_f=m
            
    
    if q==0:
        return None       
      

    return m_f
    
    

print(recurrence('ramarro','zi'))
print(recurrence('dora','am'))


            
