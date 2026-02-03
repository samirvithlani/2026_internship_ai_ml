#str functions
import pandas as pd

s = pd.Series(["apple","banana","cherry",12])
print(s)

s = s.str.upper()
print(s)

# s = s.str.contains("A")
# print(s)

s = s.str.startswith("A")
print(s)