import pandas as pd

match1 = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
match2 = pd.Series([100,200,300,400,500],index=["x","b","c","d","e"])

print(match1+match2)
