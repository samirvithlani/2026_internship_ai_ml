import pandas as pd

s = pd.Series([10,20,30,40])
print(s)

#apply
s = s.apply(lambda x: x*2)
print(s)


users = pd.Series(["user1","user2","user3","user4"])
print(users)

users = users.apply(lambda x: x.upper())
print(users)




