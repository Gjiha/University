# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:23:18 2023

@author: franc
"""

def sort_by_occurences(s):
    
    d = {}
    x = ''
    
    for c in s:
        d[c] = d.get(c,0) + 1
        
    d_sort = sorted(d.keys(), key=lambda x: d[x])
    
    for keys in d_sort:
        x += keys
    return x
    
    

print(sort_by_occurences(')))---))))::'))
        

#%%

def inverti_dizionario(d):
    d_final = {}
    for keys in d:
        d_final[d[keys]] = d_final.get(d[keys],[])
        d_final[d[keys]].append(keys)
    return d_final


d1= {'k0':6, 'k1':'python',6:3.14, 90: 6 }
print(inverti_dizionario(d1))

#%%

def show_board(l):
    
    max_n = len(l)
    d = {}
    
    
    for x in range(max_n):
        d[x] = d.get(x, l[x])
        
    
    for keys in d:
        print('_'*(d[keys]-1)+'#'+'_'*(max_n-d[keys]-1))
    
    

board = [2, 2, 3, 1, 4, 4]
print(show_board(board))

#%%

def liste_quadrati(l1,l2):
    x = sum(l1)
    d = {}
    
    
    for c in range(len(l2)):
        d[l2[c]] = d.get(l2[c], c+1)
    
    y = x**d[x]
    return y

print(liste_quadrati([1,2], [2,3]))

#%%
def liste_quadrati_ok(l1,l2):
    
    l = []
    p,q = 0,0
    
    if len(l1) != len(l2):
        return None
    
    while p < len(l1):
        
        l.append(l1[p]**l2[q])
        p += 1
        q += 1
        
    y = sum(l)
    return y


print(liste_quadrati_ok([1,2,5], [2,3,2]))
    
#%%

def get_min(d):
    
    
    d_sort=sorted(d.keys(), key=lambda x:x)
    print(d_sort)
    return d[d_sort[0]]
    

d = {'x': 13, 'b':12}
x = get_min(d)
print(x)

#%%

def move_max(a):
    
    x = max(a)
    del (a[a.index(x)])
    a.append(x)
    return a

lista_interi = [9,8,5,7,4,2,96,85,45]
print(move_max(lista_interi))
    
    
#%%

def max_str (l):
    
    ris = None
    
    for x in l:
        if ris == None or (len(x),x) > (len(ris),ris):
            ris = x
            
    return ris
    
    
stringhe_in_lista = [
    "Ti amo.",
    "Ciao a tutti!",
    "Il sole splende.",
    "Buon compleanno!",
    "Hai fame?",
    "Divertiti!",
    "La vita è meravigliosa.",
    "Sono una stringa di testo.",
    "La creatività è infinita.",
    "Buona giornata!",
    "Questo è un esempio.",
    "La musica mi fa sentire vivo.",
    "Questo è solo l'inizio.",
    "Sogna in grande.",
    "OpenAI è fantastico.",
    "L'amore conquista tutto.",
    "Ciao mondo!",
    "Questa è una frase casuale.",
    "Buon appetito!"
]

print(max_str(stringhe_in_lista))

#%%

def sort_by_len(l):
    l_sort = sorted(l,key = lambda x: len(str(x)))
    return l_sort

x = [2.345, 4, 5, 1, 3.4567, 2, 1.23, 5.678901, 3, 4.56789]

print (sort_by_len(x))

#%%

def sort_by_type(l):
    d_int,d_float,d_str = [], [], []
    for x in l:
        if type(x) == int:
            d_int.append(x)
        elif type(x) == float:
            d_float.append(x)
        else:
            d_str.append(x)
    l_final = d_int + d_float + d_str
    return l_final
    
l = [1, "due", 3.14, "quattro",5, 6.78, "sette", 8, 9.99]
x = sort_by_type(l)
print(x)

#%%

def somma_armonica(n,x=0):
    if n != 1:
        x = 1/n
        x += somma_armonica(n-1,x)
        return x
    else:
        c = 1/n
        return c

x = 10
c = somma_armonica(x)
print(c)

#%%

L = [1,2,3]

L.append(L)
print(L)
print(L is L[-1])





    
    
    
    
    
    
    
     