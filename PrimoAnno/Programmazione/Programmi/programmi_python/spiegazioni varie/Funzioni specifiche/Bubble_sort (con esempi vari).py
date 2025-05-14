# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:30:42 2022

@author: franc
"""
#BubbleSort-Ordinamento
a=[10, 1, 23, 4, 80, 9, 11, 4]


n = len(a)
ordinata = False
while not ordinata:
    ordinata = True
    i = 0
    while i < len(a)-1:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            ordinata = False
        i += 1
print(a)
#%% solo stringhe


def bubble_sort(a, inplace = True ):
    
    '''
    modifica l'ordinamento di una lista di stringhe da quello iniziale a crescente

    Parameters
    ----------
    a : lista di stringhe.
    inplace : se True va a creare un alias, se False va a creare un clone di a 
          Di default è True

    Returns
    -------
    b : a seconda del valore di inplace sarà un alias (default), o un clone (False)
      In ogni caso sarà una lista ordinata dalla stringa di lunghezza minore a quella maggiore

    '''
    
    if inplace:
        b=a
    else:
        b=a[:]
    
    ordinata = True
    j = 0
    
    while ordinata:  
        
        i = 0
        
        ordinata = False
        
        while i < len(b)-1-j: #!!
            
            if len(b[i]) > len(b[i+1]):
                
                b[i], b[i+1] = b[i+1], b[i]  #si scambiano le posizioni
                ordinata = True
                            
            i += 1 #conta la posizione nella lista
            
        j += 1  #la variabile j permette di esclidere l'ultimo elemento della lista, infatti viene sottratta al len(b)
    return b
    
a=['m','iu','ooiiuioohibbiac','oiuvbubu','nino','nin']
print(bubble_sort(a, False))


#%% anche valori

def bubble_sort(a, key = lambda x: x, inplace = True ):
    '''
    modifica l'ordinamento di una lista di valori

    Parameters
    ----------
    a : lista di stringhe.
    key : funzione che va a decidere che tipo di ordinamento far assumere alla lista
    inplace : se True va a creare un alias, se False va a creare un clone di a 
          Di default è True

    Returns
    -------
    b : a seconda del valore di inplace sarà un alias (default), o un clone (False)
      In ogni caso sarà una lista ordinata dal valore minore al maggiore

    '''
    
    if inplace:
        b=a
    else:
        b=a[:]
    
    ordinata = True
    j = 0
    while ordinata:        
        i = 0
        ordinata = False
        
        while i < len(b)-1-j:
            
            if key(b[i]) > key(b[i+1]):
                
                b[i], b[i+1] = b[i+1], b[i]
                ordinata = True
                            
            i += 1
            
        j +=1
    return b
    
a=['m','iu','ooiiuioohibbiac','oiuvbubu','nino','nin']
print(bubble_sort(a, len, True))
b=[10, 1, 23, 4, 80, 9, 11, 4]
x=[5,9,8,6,3,2,5,4,78,5,1,4,5,4,554545,5,1]
print(bubble_sort(b, lambda x: x, True ))
print(bubble_sort(x, lambda x: x, True ))

'''
modifica di bubble_sort per ordinare sia stringhe che int/float
'''

def nume_str( v ):
    if type(v) in (float, int):
        return (0, v)
    else:
        return (1, len(v))
    
b=[10,'uno', 1,'mario', 23, 4, 80, 'mamma', 9, 11,'gennaro', 4]
print(bubble_sort(b, nume_str, True ))



























