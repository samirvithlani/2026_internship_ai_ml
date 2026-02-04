import pandas as pd
import numpy as np

df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

#replace --->
df.replace(["not available","not mension","not value"],np.nan,inplace=True)
print(df)
df["RATING"] = df["RATING"].astype(float)
df["RATING"] = df["RATING"].fillna(df["RATING"].mean())
print(df)