# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:11:12 2021

@author: doguilmak

dataset: Created by myself. Totally random values.

"""
#%%
#  Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
import time

#%%
#  Data Preprocessing

start = time.time()
df = pd.read_csv('ads.csv')
print(df.describe().T)
print("\n", df.info())

for i in range (1, 10):    
    print(f"ad_{i}: ", df[f"ad_{i}"].sum())

#%%
#  Thompson Sampling

N = 1999  # Number of rows
d = 9  # Number of ads (columns)
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

sns.set_style('whitegrid')    
sns.histplot(data=chosen, kde=True)
plt.title("Thompson Sampling")
plt.xlabel("Ads")
plt.ylabel("Numbers of the Chosen Number")
plt.show()

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
