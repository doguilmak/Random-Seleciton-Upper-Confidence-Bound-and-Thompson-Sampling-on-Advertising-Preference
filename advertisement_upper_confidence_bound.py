# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:41:33 2021

@author: doguilmak

dataset: Created by myself. Totally random values.

"""
#%%
#  Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import time

#%%
#  Data Preprocessing

start = time.time()
df = pd.read_csv('ads.csv')
print(df.describe().T)
print("\n", df.isnull().sum())
print("\n", df.info())

for i in range (1, 10):    
    print(f"ad_{i}: ", df[f"ad_{i}"].sum())

#%%
#  Upper Confidence Bound(UCB)
#  Learns from past experiences

N = 1999
d = 9

#  Ri(n)
rewards = [0] * d  # All the rewards are equal to 0
#  Ni(n)
clicks = [0] * d  # Numbers of clicks

summation = 0  # Summation reward
chosen = []
for n in range(1, N):
    ad = 0   # Chosen ad
    max_ucb = 0
    for i in range(0, d):
        if(clicks[i] > 0):
            mean = rewards[i] / clicks[i] #  Ri(n)/Ni(n)
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
    
sns.set_style('whitegrid')    
sns.histplot(data=chosen, kde=True)
plt.title("Upper Confidence Bound")
plt.xlabel("Ads")
plt.ylabel("Numbers of the Chosen Number")
plt.show()

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
