import pandas as pd

s = pd.Series([1,2,3,4,5])
#print(s)

s1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
#print(s1)

s2 = pd.Series({"Maths":90,"Science":85,"English":92,"Hindi":88},dtype=float)
print(s2)