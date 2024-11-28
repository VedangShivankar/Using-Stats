import pandas as pd

ops = pd.read_csv("rev3.csv")
print(ops.head)

print(ops.plot(x= 'company', y= 'revenue', kind='bar'))