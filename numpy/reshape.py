import numpy as np

#np.reshape(array,new_shape)
#array.reshape(new_shape)

#10 -->
a = np.array([1,2,3,4,5,6])
print(a)
print(a.shape)

a1 = a.reshape(2,3)
print(a1)
print(a1.shape)

a2 = a.reshape(3,2)
print(a2)
print(a2.shape)

x = np.arange(12)
print(x)


#-1
x3 = np.arange(12)
b1 = x3.reshape(3,-1)
print(b1)

x4 = np.arange(12)
b2 = x4.reshape(-1,3)
print(b2)
