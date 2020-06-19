# for learning about the data frames in the pandas
# dataframe is a tabular datastructure similar to the spreadsheet in excel.


import pandas as pd

data = {
    'color': ['green', 'blue', 'red', 'black'],
    'object': ['pen', 'paper', 'book', 'printer'],
    'price': [3, 32, 12.12, 32]
}

dataframe = pd.DataFrame(data)
print(dataframe)
# print(dataframe.values)

frame = pd.DataFrame(data, columns=['object', 'price'])
print(frame)
