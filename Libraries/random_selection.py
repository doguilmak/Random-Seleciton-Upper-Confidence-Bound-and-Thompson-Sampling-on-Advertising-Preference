# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:28:57 2021

@author: doguilmak
"""


def random_selection(df):		
    N = df.shape[0]
    d = df.shape[1]
    
    import random
    summation = 0
    chosen = []    
    for n in range(0, N):
        ad = random.randrange(d)
        chosen.append(ad)
        reward = df.values[n, ad]
        summation = summation + reward
        
    print('Total Reward:')
    print(summation)