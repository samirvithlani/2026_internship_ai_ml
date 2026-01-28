import numpy as np

a = np.arange(12).reshape(3,4)
print(a)
print(a.shape)

a1 = a.flatten()
print(a1)
print(a1.shape)

x1 = np.arange(24).reshape(4,3,2)
print(x1)
print(x1.shape)

b2 = x1.flatten()
print(b2)
print(b2.shape)


x3 = np.arange(12).reshape(4,3)
print(x3)

#column

b3 =  x3.flatten(order="F")
print(b3)
print(b3.shape)



b4 = x3.flatten(order="C")
print(b4)
print(b4.shape)

#memory order
b4 = x3.flatten(order="K")
print(b4)
print(b4.shape)
