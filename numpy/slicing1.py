import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
#1  2  3  4  5
#0  1  2  3  4
#-5 -4 -3 -2 -1
print(arr[1])
print(arr[1:])
print(arr[:3])
print(arr[1:10])
print(arr[-1])
print(arr[:-1])
print(arr[-2:])

print(arr[0:10:2])
print(arr[::2])