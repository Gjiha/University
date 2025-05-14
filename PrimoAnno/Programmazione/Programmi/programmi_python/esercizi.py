# In[0]

def sort_by_occurences (x):

    d = {}
    i = ''

    if len(x) == 0:
        return 0
    
    else :
        for c in x:
            d[c] = d.get(c,0) + 1

        d_sort = sorted(d.keys(), key = lambda x: d[x])

        for keys in d_sort:
            i += keys
        return i
    
x = print(sort_by_occurences(')))---))))::'))

# In[1]

def valute_comb(x,z, key = 'EUR'):

    d = {'USD': 1.0, 'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.74}

    try:
        y = x/d[key]
        y = y*d[z]
        return y
    except KeyError:
        return('la valuta non è supportata o inesistente')

print(valute_comb( 0.85, 'PY'))

# In[2]

def no_duplicate(list):

    d = {}

    for x in list:
        d[x] = d.get(x,0) + 1
    
    d_sort = sorted(d.keys(), key = lambda x: d[x])
    return d_sort

x = [5,5,5,5,5,4,4,4,4,3,3,2,2,2,1,1,0]
print(no_duplicate(x))

# In[3]

def inverti_dizionario(d1):

    d_final = {}

    for key in d1 :
        d_final[d1[key]] = d_final.get(d1[key],[])
        d_final[d1[key]].append(key)
    
    return d_final


d = {'USD': 110.0, 'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.85}
print(inverti_dizionario(d))
        
# In[4]

def ordina_dizionario(d, reverse = False, jessica = True):  #jessica intende le chiavi

    if jessica:
        d_sort = sorted(d.keys(),reverse = reverse)
    else:
        d_sort = sorted(d.values(), reverse = reverse)
    
    return d_sort


d = {'USD': 1.0, 'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.74}
print(ordina_dizionario(d,jessica = False))

# In[5]

def max_dict(d,mx=True):

    if mx:
        d_f = max(d.keys(),key = lambda x: d[x])
    else:
        d_f = min(d.keys(),key = lambda x: d[x])
    return d_f

d = {'USD': 1.0, 'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.74}
print(max_dict(d))

# In[6]

def dict_intersection (d1,d2):

    if len(d1.keys()) >= len(d2.keys()) :
        D1 = d1
        D2 = d2
    else:
        D1 = d2
        D2 = d1
    
    for keys in D2:
        D1[keys] = D1.get(keys, 0) + D2[keys]
    
    return D1

d1 = {'a': 1, 'b': 2, 'c': 3,'e':9}
d2 = {'b': 10, 'c': 20, 'd': 30}
print(dict_intersection(d1,d2))


# In[7]

def dict_union(d1,d2):
     
    if len(d1.keys()) >= len(d2.keys()) :
        D1 = d1
        D2 = d2
    else:
        D1 = d2
        D2 = d1
    
    for key in D2:
        try:
            D1[key] = [(D1[key])]
            D1[key].append(D2[key])
        except KeyError:
            D1[key] = D1.get(key,D2[key])
    
    return D1

d1 = {'a': 'mamma', 'b': 2, 'c': 3,'e':9}
d2 = {'b': 'pa', 'c': 20, 'd': 30}
print(dict_union(d1,d2))

# In[8]

def print_list(l):

    Str,Float,Int=[],[],[]
    s,f,i = 0,0,0

    if len(l)==0:
        print("la stringa è vuota")
        return
    else:
        for c in l:
            if type(c)==int:
                Int.append(c)
                i += 1
            elif type(c)==float:
                Float.append(c)
                f += 1
            else:
                Str.append(c)
                s += 1
        x = [s,i,f]
        t = min(x)
        for c in range(t):
            print(Int[c],Float[c],Str[c],"\n")
        return
    
x = ['a','b','c','d',1,2,3,4,1.5,2.5,3.5,4.5]
print_list(x)


# In[]

def muted_by_freq(l):
    d = {}
    i = 0

    if len(l) == 0 or len(l) == 1:
        return l

    for c in l:
        d[c] = d.get(c,0) + 1
    
    sort_dict = sorted(d.keys(), key= lambda x: d[x])
    
    for c in sort_dict:
        t = 0
        while t < d[c]:
            l[i] = c
            i += 1
            t += 1
    return l


L = ['a', 4, 2, 2,2,2,2, 'b', 'b', 'b']
print(muted_by_freq(L))


# In[]
'''
def division_reiterable(x):
    c = 2
    while c < x:
        if x%c == 0:
            return None
        c += 1 
    return (x)

def list_non_divisible(y):
    l = []
    for c in range(y):
        if c == 0:
            continue
        elif c == 1 or c == 2:
            l.append(c)
        else:
            x = division_reiterable(c)
            if x != None:
                l.append(c)
    return l
'''

def list_non_divisible(y):
    l = []
    num_no_prime = [True]*y
    for num in range(1,y):
        if num == 1:
            l.append(num)
            num_no_prime[num] = False
        elif num_no_prime[num]:
            l.append(num)
            for c in range(num*2,y,num):
                num_no_prime[c] = False
    return l
    
print(list_non_divisible(100))


# In[]

def union_values(x,y):
    d = {}
    d1_val = list(d1.values())
    d2_val = list(d2.values())
    l = []

    for c in d1_val:
        d[c] = d.get(c,-20)
    for t in d2_val:
        d[t] = d.get(t,0)*-1
    for k in list(d.items()):
        if k[1] > 0:
            l.append(k[0])
    return l


d1 = {'a': 1, 'b': 2, 'c': 3,'e':9}
d2 = {'b': 1, 'c': 20, 'd': 9}
print(union_values(d1,d2))

#%%
d = {'b': 1, 'c': 20, 'd': 9}
l = list(d.values())
l1 = [0]*len(l)
l2 = list(zip(l,l1))
print(l2)


# In[]

l = []
i = 0
while i<(20-12):
    l.append(12+i)
    i += 1
print(l)



# %%

k = ''
d0,d1 = {},{}
for i in range(10):
    d0[k+'x'] = i
    d1[i]= k+'x'
    k += 'x'
print(d0[d1[3]+d1[4]])

# %%

def f(x):
    if type(x)==type(0):
        return x
    else:
        return -1

a = ['a','b',0,7,8,'p','o']
a.sort(key = f)
print(a)

# %%
