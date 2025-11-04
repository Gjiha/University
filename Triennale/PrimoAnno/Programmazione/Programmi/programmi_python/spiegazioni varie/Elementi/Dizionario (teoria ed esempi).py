# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:01:41 2022

@author: franc
"""
#%%

                #NOZIONI BASE DEI DIZIONARI

d={} #dizionario vuoto
d1= {'k0':6, 'k1':'python',6:3.14 }

#lettura
print( d1['k1'] )
#print( d1['k9'] ) # non è una chiave del dizionario e quindi dà errore

if 'k9'in d1: #stabilisce se la chiave è corretta
    print( d1['k9'] )

#scrittura, come nelle liste

if 'k9'in d1: 
    print( d1['k9'] )
else:
    d1['k9']='cappanove'


d1[6]='sei'


#eliminazione

del(d1[6])

# confronto

d1 == d # se i due dizionari sono IDENTICI retituirà True

#somma fra elementi dentro una lista in un dizionario 
d2={'j':[9]}
d2['j']=d2['j'][0]+7
print(d2)




#%%
'''
inizio teoria e funzionamento più esempi del metodo get
'''

#%% METODI
#prova del metodo get

d={'a':6, 'b':9}
print( d.get('a') )
print( d.get('h') ) #con il metodo get non c'è errore, invece che con l'indicizzazione   
print( d.get('a',0) )
y=d.get('h',9) 
d['h']=y
print(d)

# metodo keys

a = d.keys() # ritorna una lista con le chiavi

# metodo values

b = d.values() #ritorna una lista con i valori

# metodo items

c = d.items()
#ritorna una lista di tuple con le coppie chiavi/valori


#%%

# !! ESECUZIONE DEL METODO GET !!

def prova_dizio(lista):
    d = {}
    
    for x in lista:
        l = len(x)
        
        a = d.get(l,[]) #!!! la lista è vuota altrimenti il metodo get salva il valore, cosa molto importante da ricordare 
        a.append(x)  # METTERE SEMPRE una lista VUOTA o un valore NULLO per usare il metodo get se si vuole aggiornare d
        
        d[l] = a
        
    return d 


x=['mamma','ao','a','aoa','bb','aoaoao']
print(prova_dizio(x))
        
        
