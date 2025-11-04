#%%
def initials(a):
    
    d = {}
    
    l = []

    l = a.split() 
    
    for c in l:
        d[c[0]] = d.get(c[0],[])
        
        d[c[0]].append(c)
        
    
    return d


a = 'questo è un mondo Om Oa 1 1234 43 4odio omondibaibaibcibca ma lo aaaaaaaaaaaaa tanto tantissimo p papà uomo éolo'
print(initials(a))
# %%
