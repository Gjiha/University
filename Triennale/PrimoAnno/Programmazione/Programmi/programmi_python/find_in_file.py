# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:26:27 2022

@author: franc

"""
#%%
def find_in_file( filename, k):
    '''
    

    Parameters
    ----------
    filename : una stringa contenente il nome di un file
    k : una stringa contenente ila stringa ricercata nel file

    Returns
    -------
    c : una tupla che a due a due indica la linea di codice dove si trova la stringa k nel primo valore
          e nel secondo indica la posizione di k all'interno della linea'
    '''
        
    
    f=open(filename)
    c,t=[],1           
    
    for line in f :  
        
        for x in range(len(line)-len(k)+1):
           
            if k==line[x:x+len(k)]:          
                
                c.append( (t, x) )       
            
        t+=1
        
        j=tuple(c)      


    f.close()  
    
    return j

print(find_in_file('find_in_file.py', 'line'))




#%%


def find_in_file( filename, k):
        
    
    f=open(filename)
    c,t=[],1        #O(1)
    
    for line in f :  #O(n)
        
        if k in line: #O(1)  \    O(m)
            
            c.append(t)  #O(1)
                    
        t+=1    #O(1)
        
    f.close()   #O(1)
    
    j=tuple(c)  #nel caso peggiore O(n)
    
    return j

print(find_in_file('Browse_dir.py', 'file'))

# poichè il costo era quadratico lavorando con le tuple, lavoriamo con le liste che poi vengono trasormate in tuple

# costo totale n

#  \ costo totale nm, il costo della funzione è O(nm)
       







            
        






