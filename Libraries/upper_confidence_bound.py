# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:25:26 2021

@author: doguilmak
"""


def upper_confidence_bound(df):
    import math
    N = df.shape[0] #  Number of rows
    d = df.shape[1] #  Number of ads (columns)
    
    #  Ri(n)
    rewards = [0] * d  #  All the rewards are equal to 0
    #  Ni(n)
    clicks = [0] * d  # Numbers of clicks
    
    summation = 0  #  summation reward
    chosen = []
    for n in range(1, N):
        ad = 0  # Chosen ad
        max_ucb = 0
        for i in range(0, d):
            if(clicks[i] > 0):
                mean = rewards[i] / clicks[i]  # Ri(n)/Ni(n)
                delta = math.sqrt(3/2 * math.log(n) / clicks[i])
                ucb = mean + delta
            else:
                ucb = N * 10
            if max_ucb < ucb:  # Looking for highest UCB
                max_ucb = ucb
                ad = i          
        chosen.append(ad)
        clicks[ad] = clicks[ad] + 1
        reward = df.values[n, ad]
        rewards[ad] = rewards[ad] + reward
        summation = summation + reward
    
    print('Total Reward:')   
    print(summation)  # Highest UCB value
    return summation
