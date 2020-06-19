# data_structure.py

import numpy as np
import pandas as pd

series_ = pd.Series([32, 23, 31, 30])
print(series_)

s2 = pd.Series([32, 1, 13, 43], index=['a', 'b', 'c', 'd'])
print(s2)
print(s2.index)
print(f"The length of data s2 series is {len(s2)}")


random_series = np.random.randint(-5, high=255, size=(10,))
print(random_series)

rand_series = pd.Series(random_series)
print(rand_series)

data_ = pd.Series([23, 41, -10, 32, -30, 41])

log = np.log(data_[:])
print(log)

print(log[log.isnull()])

print("======")
print(log[log.notnull()])
