import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)


data = {
    "Name":["raj","amit","sumit"],
    "Age":[21,22,23],
    "City":["Delhi","Mumbai","Bangalore"]
}

df = pd.DataFrame(data)
print(df)


#df1 = pd.DataFrame([[1,2],[3,4]])
df1 = pd.DataFrame([[1,2],[3,4]],columns=["data1","data2"])
print(df1)

#np array

df2 = pd.DataFrame(np.array([[1,2],[3,4]]),columns=["data1","data2"])
print(df2)