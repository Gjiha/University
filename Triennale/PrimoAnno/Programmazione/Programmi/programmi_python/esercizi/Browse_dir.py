# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:36:17 2022

@author: franc
"""



import os 


#%%

def browse_dir( d ):
    '''
    prende in imput una cartella e in output printa tutti i file presenti
    se all'interno della cartella ve n'è presente un'altra la apre
    
    '''
    cartella = os.listdir(d)
    
    for x in cartella:
        full_path = os.path.join(d, x)
        
        if os.path.isfile(full_path):
            print(f'FILE: {full_path}')
        
        elif os.path.isdir( full_path ):
            browse_dir( full_path )
            
browse_dir( os.getcwd() )

#%%

def browse_dir( d , txt ):
    '''
    prende in imput una cartella e una stringa
    metterà in una lista tutti i file nei quali è presente la stringa in imput

    '''
    cartella = os.listdir(d)
    b = []
    
    for x in cartella:
        full_path = os.path.join(d, x)
        
        if os.path.isfile(full_path) and full_path.split('.')[-1] == 'py':  
            f = open(full_path)
            for line in f:
                if txt in line:
                    b.append(full_path)
                    break
            f.close()
        
        elif os.path.isdir( full_path ):
            c = browse_dir( full_path, txt=txt )
            b.extend(c)
    return b
            
browse_dir( os.getcwd(), 'os' )







    



