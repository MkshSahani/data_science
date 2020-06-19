# for reading csv file

import pandas as pd

data_ = pd.read_csv('csv_data.csv')
print(data_)
print(type(data_))
data_ = pd.DataFrame(data_)
print(data_)
print(type(data_))
id_ = data_.iloc[:, 0].values
print("id : ", id_)
names_ = data_.iloc[:, 1].values
print("names : ", names_)
address_ = data_.iloc[:, 2].values
print("Address : ", address_)
rating_ = data_.iloc[:, 3].values
print("Rating  : ", rating_)
