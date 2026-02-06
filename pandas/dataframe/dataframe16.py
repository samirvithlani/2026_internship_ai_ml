import pandas as pd

df  = pd.read_csv("bengaluru_house_prices.csv")
#print(df.head())

#n_largest
x = df["price"].nlargest(5)
print(x)

x1 = df.nlargest(5,"price")
print(x1)

#n_smallest
# x2 = df["price"].nsmallest(5)
# print(x2)

# x3 = df.nsmallest(5,"price")
# print(x3)

#area

#area = df.value_counts("location")
#print(area)

#group by

location = df.groupby("location")
#print(location.groups)

x = location.get_group("Electronic City")
print(x)

#doubt..
