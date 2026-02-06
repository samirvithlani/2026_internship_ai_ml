import pandas as pd

df1 = pd.DataFrame({"Fruit":["apple","banana","orange","grape"],"vegitables":["potato","tomato","ladyfinger","carrot"],"Market_Price":[100,40,80,60]})
df2 = pd.DataFrame({"Fruit":["apple","banana","grape","kiwi"],"vegitables":["potato","tomato","cabbage","carrot"],"Shop_Price":[120,50,90,70]})



#x = pd.merge(df1,df2,on=["Fruit","vegitables"],how="inner")
x = pd.merge(df1,df2,on="vegitables",how="inner")
print(x)
