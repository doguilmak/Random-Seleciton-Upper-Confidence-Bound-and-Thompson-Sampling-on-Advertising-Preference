# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:29:14 2021

@author: doguilmak

dataset: Created by myself. Totally random values.

"""
#%%
#  Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
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
#  Random Selection
    
import random
#  Trying to find most clicked ad
N = 1999  # 1999 rows in dataframe
d = 9  # 9 columns in dataframe
summation = 0
chosen = []
for n in range(0, N):
    ad = random.randrange(d)
    chosen.append(ad)
    odul = df.values[n, ad]
    summation = summation + odul

print('Total Reward:')   
print(summation)  # Highest UCB value
    
sns.set_style('whitegrid')    
sns.histplot(data=chosen, kde=True)
plt.title("Random Selection")
plt.xlabel("Ads")
plt.ylabel("Numbers of the Chosen Number")
plt.show()

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
