import pandas as pd

df1 = pd.DataFrame({"Fruit":["apple","banana","orange","grape"],"Market_Price":[100,40,80,60]})
df2 = pd.DataFrame({"Fruit":["apple","banana","grape","kiwi"],"Shop_Price":[120,50,90,70]})


#x = pd.merge(df1,df2,on="Fruit",how="inner")
#x = pd.merge(df1,df2,on="Fruit",how="outer")
#x = pd.merge(df1,df2,on="Fruit",how="left")
x = pd.merge(df1,df2,on="Fruit",how="right")
print(x)


