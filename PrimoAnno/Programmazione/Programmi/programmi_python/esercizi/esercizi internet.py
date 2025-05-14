# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:42:01 2023

@author: franc
"""
'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket,
 che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo.
 Ad esempio la parola "mangiare" diventa "momanongogiarore".

Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket.
 Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra,
 e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.
'''

def traduzione_1 (x):
    
    l = []
    c = 0
    d = {'a':0,'e':0,'i':0,'o':0,'u':0}
    
    while c < len(x):
        if x[c] in d:
            l.append(x[c])
            c += 1
        else:
            l.append(x[c])
            c += 3
            
    
    s = ''.join(l)
    return s


s = "momanongogiarore"
print (traduzione_1(s))
            
#%%

def traduzione_2 (x):
    
    d = {'a':0,'e':0,'i':0,'o':0,'u':0}
    l= []
    
    for c in range(len(x)):
        if x[c] in d:
            l.append(x[c])
        else:
            l.append(x[c]+'o'+x[c])
            
    s = ''.join(l)
    return s

s = "mangiare"
print (traduzione_2(s))

#%% 





        
 
 