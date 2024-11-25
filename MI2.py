import pandas as pd 
import seaborn as sn


crunching = pd.read_csv("heights.csv")
print(crunching.head())
print(crunching.height.describe())
print(sn.histplot(crunching.height, kde=True))

mean = crunching.height.mean()
print(mean)
stdev = crunching.height.std()
print(stdev)
print(mean - 3*stdev)
print(mean + 3*stdev)

print(crunching[crunching.height < 54.82])
print(crunching[crunching.height > 77.91])
print(crunching[(crunching.height < 54.82) | (crunching.height > 77.91)])
no_outlier = crunching[(crunching.height > 54.82) & (crunching.height < 77.91)]
print(no_outlier)

crunching['zscore'] = (crunching.height-crunching.height.mean())/crunching.height.std()
print(crunching.head())
print(crunching[(crunching.zscore<-3)|(crunching.zscore>3)])
print(crunching[(crunching.zscore>-3)&(crunching.zscore<3)])