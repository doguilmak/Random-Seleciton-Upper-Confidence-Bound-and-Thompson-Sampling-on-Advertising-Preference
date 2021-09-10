# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:24:26 2021

@author: doguilmak
"""


def thompson_sampling(df):
    import random
    N = df.shape[0]  # Number of rows
    d = df.shape[1]  # Number of ads (columns)
    summation = 0  # Summation reward
    chosen = []  # Ni(n) 
    ones = [0] * d
    zeros = [0] * d
    for n in range(1, N):
        ad = 0  # Chosen ad
        max_th = 0
        for i in range(0, d):
            rasbeta = random.betavariate(ones[i] + 1, zeros[i] + 1)
            if rasbeta > max_th:
                max_th = rasbeta
                ad = i
        chosen.append(ad)
        reward = df.values[n, ad]
        if reward == 1:
            ones[ad] = ones[ad] + 1
        else:
            zeros[ad] = zeros[ad] + 1
        summation = summation + reward    
        
    print('Total Reward:')   
    print(summation)
    return summation
