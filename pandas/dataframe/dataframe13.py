import pandas as pd


people1 = {"First":["hardik","amit","sumit","raj"],
"Last":["shah","patel","thakkar","shah"],
"Email":["hardik","amit","sumit","raj"]}

df = pd.DataFrame(people1)
#print(df)
df["Full Name"] = df["First"] + " "+ df["Last"]
#print(df)

#df.drop
df.drop(columns=["First","Last"],inplace=True)
#print(df)

df[["First","Last"]] = df["Full Name"].str.split(" ",expand=True)
#print(df)


x = df.pop("Full Name")
print(x)
print(df)