import pandas as pd
import numpy as np

math = pd.read_csv("test1.csv", names=["names","income"], skiprows=[0])
print(math)

print(math.describe())
print(math.income.quantile(0.75,interpolation="higher"))

ridder = math.income.quantile(0.99)
print(math[math.income>ridder])

ridding = math[math.income<=ridder]
print(ridding)

