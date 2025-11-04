# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:17:30 2022

@author: franc
"""
#%%
def conta_birre_ric(k1,k): 

    k_ric = k1//k     #O(1)   
    return k_ric

def conta_birre_max(d,p,k):
    if d >= p:                   #O(1) 
        x = d//p #birre bevute   #O(1)     
        t = conta_birre_ric(x, k)  #O(1) 
        c=t+x                  #O(1) 
        
        while t >= k:  #O(n/2) 
            t1 = conta_birre_ric(t, k)
            c += t1
            t = t1-k+t 

    return c


print(conta_birre_max(15, 1, 3))


#%%
'''
inizio esercizi con ricorsione
'''
#%%  
    
def fattoriale(x, d=0):
    if x < 0:
        return None
    elif x == 0 :
        return 1
    else:
        d += 1 
        y = x-1
        z = fattoriale(y,d)
        
    return z*x



print(fattoriale(5))

#%% sequenza di mailstorn

def mail_ric(x,d):
      
    if x == 1:       
        return d
        
    elif x%2 == 0:
        j = x/2
        d.append(j)
        return mail_ric(j,d)
    
    else:
        j = (3*x)+1
        d.append(j)
        return mail_ric(j,d)
    
def mail_final(x):
    
    if x <= 0:
        return None
    else:
        d=[x]
        y=mail_ric(x,d)
        return y
        
    
print(mail_final(9))

#%% palindroma ricorsiva
def del_string(x):
    string =x
    characters = "'!? "

    for x in range(len(characters)):
        string = string.replace(characters[x],"")

    return string
    


def palindrome(y):
    
    x=del_string(y)
   
    n = len(x)
    
    if n == 1 or ( n == 2 and x[0] == x[len(x)-1]): 
        return True
    
    elif n > 1 and x[0] == x[len(x)-1]:
        return palindrome(x[1:len(x)-1])
    
    else:
        return False
        

        
print(palindrome("m'am!!mam"))

#%% palindroma con while

def palindrome(x):
    string = x
    characters = "'!? "

    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    y = string
    p, q = 0, len(y)
    
    while p < q:
        if y[p] == y[q-1]:
            p += 1
            q -= 1
        else:
            return False
    return True

print(palindrome('ant?!!na'))
        
    
    
   
    
    
 

    


    
    
    
    
    