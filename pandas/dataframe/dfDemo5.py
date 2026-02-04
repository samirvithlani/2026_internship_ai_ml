import pandas as pd

#df = pd.read_csv("Movieratingdata1.csv")
#df = pd.read_csv("Movieratingdata1.csv",na_values=["not available","not mension"])
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
#df = pd.read_csv("Movieratingdata1.csv",na_values={"PRODUCTION_YEAR":"not available"})
df = pd.read_csv("Movieratingdata1.csv",na_values={"PRODUCTION_YEAR":["not available","not mension"]})
print(df)