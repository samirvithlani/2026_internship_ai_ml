import pandas as pd
import numpy as np

data = {
    "Name":["raj","amit","sumit","kunal","Neha","Sumit","Sandhya"],
    "Age":[21,22,23,24,25,26,27],
    "City":["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Bangalore","Delhi"]
}

df = pd.DataFrame(data)
#df["Age"] = df["Age"] + 1
# df["Age"] = [22,23,24,25,26,27,28]
# print(df)

#df = df.drop("Age",axis=1)
#df = df.drop("Age",axis=1)
df = df.rename(columns={"Age":"Student Age"})
print(df)

#add new raw
#reserch
#add column
#born year
