import pandas as pd
from thompson_sampling import thompson_sampling
from upper_confidence_bound import upper_confidence_bound
from random_selection import random_selection

df = pd.read_csv('ads.csv')

thompson_sampling(df)
upper_confidence_bound(df)
random_selection(df)
