import pandas as pd

users = pd.Series([21,22,23,21,24,25],index=["amit","raj","sumit","rohit","jay","virat"])
print(users.sample())

print(users+1)
print(users-1)
print(users*2)
print(users/2)