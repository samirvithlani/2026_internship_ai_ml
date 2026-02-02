import pandas as pd

s = pd.Series([10,20,30,0,None,40,None,50])
print(s)
print(s.isnull())
print(s.isnull().sum())
print(s.notnull())
print(s.notnull().sum())

s = s.fillna(0)
print(s)
print(s.isnull().sum())



s = pd.Series([10,20,30,0,None,40,None,50])
print(s)
s = s.dropna()
print(s)