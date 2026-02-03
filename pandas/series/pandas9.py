import pandas as pd

s = pd.Series([10,20,11,22,45,30,0,50],index=["z","b","x","d","p","f","g","h"])
#sorting
print(s.sort_values())
print(s.sort_values(ascending=False))
#print(s.sort_values(ascending=True))

#sorting index
print(s.sort_index())
print(s.sort_index(ascending=False))



