from sympy.abc import lamda
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
df["MOVIE_TITLE"] = df["MOVIE_TITLE"].astype(str)

#apply
x = df["MOVIE_TITLE"].apply(len)
#print(x)

df["MOVIE_REVIEW"] = df["RATING"].apply(lambda x: "good" if x>6 else "bad")
#print(df)

df["MOVIE_UPPER"] = df["MOVIE_TITLE"].apply(lambda x: x.upper() if x!=0 else "")
print(df)