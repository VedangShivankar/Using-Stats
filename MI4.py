import pandas as pd
import seaborn as sns 
import numpy as np

ops = pd.read_csv(
    "anoinc4.csv",
    index_col = None,
    names=["income","count"],
    skiprows=1
)
print(ops.head())

sns.set(rc={'figure.figsize':(11.7,8.27)})
g= sns.barplot(x='income',y='count', data=ops)
g.set_xticklabels(g.get_xticklabels(),rotation=45,horizontalalignment='right'
);