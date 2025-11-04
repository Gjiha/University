# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:44:10 2023

@author: franc
"""

#%% 
# creazione di una lista

l = []

# all'interno della lista possiamo mettere qualsiasi tipo di dato

d = [True, 'stringa', 10, 2.5, ('tupla', 'con più valori'), ['anche altre liste'], 'posizione 6']

# due liste si possono concatenare fra di loro grazie all'operatore +  !!SOLO LISTE!!

m = ['prova concatenazione']

z = d + m
print(z)

# una lista può essere ripetuta più volte con l'operatore * seguito da un int   !!NO FLOAT!!

w = m*2
print(w)

# si può selezionare un valore specifico specificando la posizione in cui si trova

x = d[6]
print(x)

# di può anche eliminare un valore da una lista utilizzando la funzione del

t = ['prova cancellazione', 'non', 'funziona']
del(t[1])
print(t)

# per aggiungere un valore ad una lista non conviene usare la concatenazione poichè utilizza un alto costo computazionale
#       per questo si usa il metodo append che permette di aggiungere un valore ad una lista con un costo costante

X1 = 'prova append'
m.append(X1)                 # il metodo append permette di aggiungere qualsiasi tipo di valore

    #!! ATTENZIONE L'APPEND NON RITORNA NULLA QUINDI VA USATO DA SOLO SENZA ASSOCARLO A NULLA !!!!!

print(m)  

# per aggiungere ad una lista più valori definiti come un iterabile invece di eseguire un ciclo for bisogna utilizzare il metodo extend

X2 = [] 
X2.extend(range(10)) 
print(X2)           

# quando si danno due nomi diversi ad una stessa lista si viene a creare un alias 

x2 = m   # ora x2 è l'alias di m
x2.append('prova alias')
print(m)   # andando a modificare l'alias vado a modificare anche l'originale

# diversamente dall'alias abbiamo il clone

c = ['prova clonazione']
c1 = c[:]  # il clonee si genera grazie ad uno slicing vuoto
c.append('originale')
c1.append('clone modificato')  # una volta effettuata la clonazione le due liste sono diverse in tutto e per tutto
print(c)
print(c1)

# per ordinare una lista si può usare il metodo sort
#il metodo sort permette di ordinare qualsiasi tipo di valore

s = [6,5,4,8,5,2,1,3,6,5,4]
s.sort()
st = ['mamma','ao','b','miopadre']  # se si usa su una lista di stringhe le ordina in ordine alfabetico guardando la prima lettera
st.sort()
print(s)
print(st)








































