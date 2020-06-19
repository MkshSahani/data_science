# series.py
import pandas as pd

mydict = {'red': 100, 'blue': 320, 'green': 200, 'black': 400}
orders = ['pink', 'purple', 'orange', 'brown']
series_data = pd.Series(mydict, index=orders)
print(series_data)
