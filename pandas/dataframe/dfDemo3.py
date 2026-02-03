import pandas as pd
import numpy as np

data = {
    "Name":["raj","amit","sumit","kunal","Neha","Sumit","Sandhya"],
    "Age":[21,22,23,24,25,26,27],
    "City":["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Bangalore","Delhi"]
}

df = pd.DataFrame(data)

#selecting...
# print(df["Age"])
# print(df[["Age","City"]])
#print(df.iloc[0])
print(df.loc[2,"Age"])
print(df.iloc[2,1])