import pandas as pd
import numpy as np

df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
#print(df)

#df.dropna(inplace=True)
#df.dropna(inplace=True,axis=1)
#df.dropna(inplace=True,how="any")
df.dropna(inplace=True,how="all")
print(df)
