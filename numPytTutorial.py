import numpy as np
from numpy import random
'''
arr = np.array([1,2,3,4,5])
for i in arr:
    print(id(i),i)

print(type(arr))

listArr = [1,2,3,4,5]
for i in listArr:
    print(id(i),i)

print(np.__version__)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([
    [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]]
])
e = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a,b,c,d,e,sep="\n")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('----------Random----------')
#Random Values
x = random.randn()
print(x)


'''

arr = np.array([[[1,2,3],
                [1,2,3],
                [1,2,3],
                 [1,2,3]],
                [[1,2,3],
                 [1,2,3],
                 [1,2,3],
                 [1,2,3]]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(np.arange(1,10000))