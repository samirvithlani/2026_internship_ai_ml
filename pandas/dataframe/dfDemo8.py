import pandas as pd
import numpy as np

df = pd.read_csv("Movieratingdata1.csv")
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

df.drop("MOVIE_TITLE",axis=1,inplace=True)
print(df)