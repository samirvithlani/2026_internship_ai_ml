import pandas as pd

s = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(s)
print(s['a'])
print(s[0])

#loc
print(s.loc['c'])
#iloc
print(s.iloc[2])

print("at",s.at['c'])
print("iat",s.iat[2])

#label based
print(s[['a','c']])
print(s['a':'c'])

#boolean access
print(s[s>30])