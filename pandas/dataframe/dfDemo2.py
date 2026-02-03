import pandas as pd
import numpy as np

data = {
    "Name":["raj","amit","sumit","kunal","Neha","Sumit","Sandhya"],
    "Age":[21,22,23,24,25,26,27],
    "City":["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Bangalore","Delhi"]
}

df = pd.DataFrame(data)
#print(df)
# print(df.head())
# print(df.tail())
print(df.sample())
#print(df.info())
print(df.describe())

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)