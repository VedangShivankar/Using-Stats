import pandas as pd
import numpy as np

df = pd.read_csv("biglog5.csv")
print(df.head())
print(df.revenue.describe())
df['revenue_mln'] = df['revenue'].apply(lambda x: x/1000000)
print(df.revenue_mln.describe())

_, mean, std, *_ = df.revenue_mln.describe()
def get_z_score(value,mean,std):
    return (value-mean)/std

df['z_score'] = df.revenue_mln.apply(lambda x:get_z_score(x,mean,std))
print(df.head(3))

def get_mad(s):
    median = np.median(s)
    diff = abs(s-median)
    MAD = np.median(diff)
    return MAD

MAD = get_mad(df.revenue_mln)
median = np.median(df.revenue_mln)
print(MAD,median)

def get_mod_z_score(x,median,MAD):
    return .6745*(x-median)/MAD
print(get_mod_z_score(2787,median,MAD))