
import pandas as pd
s2 = pd.Series({"Maths":90,"Science":85,"English":92,"Hindi":88,"Physics":78,"Chemistry":82,"Computer":95},dtype=float)
#print(s2.head())
#print(s2.head(2))
#print(s2.tail(3))
#print(s2.tail())

print(s2.sample())
print(s2.shape)
print(s2.size)
print(s2.ndim)
print(s2.dtype)
print(s2.values)
print(s2.index)
print(s2.info())