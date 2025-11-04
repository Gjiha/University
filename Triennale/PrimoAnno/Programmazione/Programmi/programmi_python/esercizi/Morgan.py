# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:38:55 2023

@author: franc
"""

def trova_nomi(x):
    l = "Mario; Giovanni; Elena; Pina; Gino; Rino; Umberto"
    y = l.split('; ')
    d={} 
    p = 0
    
    for c in y:
        a = d.get(c,[])
        a.append(0)
        
        d[c] = a
    
    for t in x.split('; '):
        if t in d:
            p += 1
        else:
            continue
    
    return p

x = "Mario; Giovanni; Elena; Mrio"
print(trova_nomi(x))

#%%

def calcola_char (l):
    
    p = 0
    d = []
    f = []
    
    for c in l:
        p = 0
        for y in c:
            p += ord(y)
        d.append((p, c))
    
    d.sort()
    print(d)
    
    for x in d:
        f.append(x[1])
    
        
    return f

t = ['mamma','ciao','gennaro','a']
x = calcola_char(t)
print(x)

#%%

def max_list( l1, l2 ):
    
    f = []
    d = {}
    
    
    if len (l1) > len (l2):
        L = l1
        l = l2
    else:
        l = l1
        L = l2
    
    for x in L:
        d[x] = d.get(x,[])
    
    for y in l:
        if d.get(y) != None:
            f.append(y)
    
    return f

a = [5,7,(None),'mario',(0,4),True]
t = ['mamma','mario','gennaro',True]
print(max_list(a, t))

#%%

def dict_union (d1,d2):
    
    if len(d1) > len(d2) :
        D = d1
        d = d2
    else:
        D = d2
        d = d1
    
    
    
    for c in list(d.keys()):
        
        D[c] = D.get(c,[])
        if D[c] != []:
            D[c] = [D[c]]
        D[c].append(d[c])
        
    return D


d = {'a':6, 'b':9}
t = {'k0':6, 'b':'python',6:3.14 }
x = dict_union(d, t)
print(x)     



mn = {2:28}
md = {4:30, 6:30, 9:30, 11:30}
mx = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31}
y = dict_union(mn, md)
z = dict_union(y, mx)
print(z)

#%%

def dict_occur(l):
    d = {}
    
    for x in l:
        
        d[x] = d.get(x,0) + 1
    
    return d


d = [1,2,1,1,2,7]
x = dict_occur(d)
print(x)

#%%

def dict_soglia(d, s_i=0, s_c='a'):
    
    for keys in list(d.keys()):
        if type(keys) is int:
            if keys < s_i:
                del(d[keys])
        elif type(keys) is str:
            if keys < s_c:
                del(d[keys])
    
    return d


t = {'k0':6, 'b':'python',6:3.14 }
x = dict_soglia(t,7,'c')
print(x)

#%%

'''
Scrivi un programma che prenda due parole come input e determini se sono anagrammi l'una dell'altra.
Due parole sono considerate anagrammi se possono essere ottenute rimescolando le lettere dell'altra.

'''

def anagrams(s1, s2):
    if len(s1) != len(s2):
        return 'Le due stringhe non sono anagrammi'
    
    d = {}
    
    for c in s1:
        d[c] = d.get(c, 0) + 1
    
    for c in s2:
        if c not in d or d[c] == 0:
            return 'Le due stringhe non sono anagrammi'
        d[c] -= 1
    
    return 'Le due stringhe sono anagrammi'

y = "liten"
x = "silent"

z = anagrams(y, x)
print(z)

#%%

def calendar(z):
    
    l = []
    x, y = 1, 1
    d = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
    
    while x <= 12:
        while  y <= d[x]:
            l.append([y, x, z])
            y += 1
        x += 1
        y = 0
    return l

print (calendar(2023))

#%%

def prime_number(x):
    
    l = {2:0, 3:0, 5:0, 7:0}
    t = True
    
    if x in l:
        return t
    else:
        for keys in l:
            if x % keys == 0:
                t = False
    return t
            
print(prime_number(9))
            
#%%

def ceasar_cyphrary(s):
    
    f = ''
    
    d = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j',
         'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q',
         'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x',
         'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
    
    
    for c in list(s):
        f += d[c]
    return f

x = ceasar_cyphrary('mamma')
print(x)

#%%


        
    
    
    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        