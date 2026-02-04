import pandas as pd
import numpy as np

df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
print(df)
#print(df.isnull().sum())
#df.replace("not available",value=None,inplace=True)
#df.replace("not available",np.nan,inplace=True)
df.replace(["not available","not mension"],np.nan,inplace=True)
print(df)
df.replace('1390411','The Batman',inplace=True)
print(df)