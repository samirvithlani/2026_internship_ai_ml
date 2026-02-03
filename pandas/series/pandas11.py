#map
import pandas as pd

s = pd.Series([10,20,30,40])
print(s)

s = s.map(lambda x: x*2)
print(s)
