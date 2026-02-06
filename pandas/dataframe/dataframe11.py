import pandas as pd
import numpy as np
df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

df.replace(["not available","not mension","not value"],np.nan,inplace=True)
#print(df)

df.fillna(0,inplace=True)
#print(df)
df["PRODUCTION_YEAR"] = df["PRODUCTION_YEAR"].astype(int)
df["RATING"] = df["RATING"].astype(float)
#print(df["PRODUCTION_YEAR"]>2015)
#data = df[df["PRODUCTION_YEAR"]>2015]
#&
data = df[(df["PRODUCTION_YEAR"]>2015) & (df["RATING"]>8)]
print(data)

data1 = df[df["GENRES"].str.contains("War",na=False)]
print(data1)