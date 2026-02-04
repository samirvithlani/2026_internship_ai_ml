import pandas as pd
import numpy as np

df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

#replace --->
df.replace(["not available","not mension","not value"],np.nan,inplace=True)
#df.fillna(value=0,inplace=True)
#df.fillna({"MOVIE_ID":0},inplace=True)
df.fillna({"MOVIE_ID":0,"PRODUCTION_YEAR":2000},inplace=True)
print(df)