import numpy as np

'''
It is a Python library that provides a multidimensional array object
NumPy package, is the ndarray object
Changing the size of an ndarray will create a new array and delete the original.
Why Numpy fast --> Vectorization describes the absence of any explicit looping, indexing, etc.

Basics:
    NumPy’s array class is called ndarray. It is also known by the alias array. 
    Note that numpy.array is not the same as the Standard Python Library class array.array, 
        which only handles one-dimensional arrays and offers less functionality
    ndarray.ndim --> the number of axes (dimensions) of the array.
    ndarray.shape --> This is a tuple of integers indicating the size of the array in each dimension.
    ndarray.size --> the total number of elements of the array. This is equal to the product of the elements of shape.
    ndarray.dtype --> an object describing the type of the elements in the array. Additionally NumPy provides types of its own.
                      numpy.int32, numpy.int16, and numpy.float64.
    ndarray.itemsize --> the size in bytes of each element of the array.
    ndarray.data --> the buffer containing the actual elements of the array.

Array Creation:
    The type of the array is explicitly defined using the dtype np.array([1,2,3],dyte=complex)
Operation:
    Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.
    a.min()
    a.sum()
    a.max()
Universal Functions:
    NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc).

NumPy gives you an enormous range of fast and efficient ways of creating arrays and manipulating numerical data inside them.
NumPy arrays are faster and more compact than Python lists.

ndarray is created using np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(), dtype
    np.linspace() to create an array with values that are spaced linearly in a specified interval

Reshape:
    Using arr.reshape() will give a new shape to an array without changing the data. 
    Just remember that when you use the reshape method, 
    the array you want to produce needs to have the same number of elements as the original array.
        np.arange(1,25).reshape(5,5)

Indexing and Slicing:
    arr[0:3]
    arr[:,0:3]

Basic Operations:
    five = (a>=5)
    print(arr[five])
    gt[arr>5] all the values greater than 5 will be added to gt array.
    You can also add multiple conditions like if in the array.
    c=a+b
    NumPy understands that the multiplication should happen with each cell. That concept is called broadcasting.

Using the copy method will make a complete copy of the array and its data (a deep copy).
You can use the view method to create a new array object that looks at the same data as the original array
You can find the unique elements in an array easily with np.unique.
You can transpose your array with arr.transpose() or You can also use arr.T
NumPy’s np.flip() function allows you to flip, or reverse, the contents of an array along an axis. 
You can use flatten method to flatten your array into a 1D array.







'''

print("--------------------Basics--------------------")
arr1 = np.arange(1, 26).reshape(5, 5)
print("The two Dimentional Array is\n", arr1)
print("The dimensional of the array is", arr1.ndim)
print("The shape of the array is", arr1.shape)
print("The size of the array is", arr1.size)
print("The type of the array is", type(arr1))
print("The data type of the array is", arr1.dtype)
print("The itemsize of the array is", arr1.itemsize)

print("--------------------Array Creation--------------------")
arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)
explicitArrayType = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
print("explicit Array type is\n", explicitArrayType)
explicitFloatArrayType = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print("explicit float Array type is\n", explicitFloatArrayType)
prodArr1 = np.array([1, 2, 3, 4, 5])
prodArr2 = np.array(([6, 7, 8, 9, 10]))
print("The prod array is", prodArr1 * prodArr2)
print("The prod array is", prodArr1 @ prodArr2)
print("The prod array is", prodArr1.dot(prodArr2))
print("The addition array is", prodArr1 + prodArr2)
print("The difference array is", prodArr2 - prodArr1)

zeroArr = np.zeros((3, 2))
print("The Zero Array's are\n", zeroArr)
onesArr = np.ones((4, 3), dtype=complex)
print("The Ones Array's are\n", onesArr)
emptyArr = np.empty((3, 2))
print("The Empty array is\n", emptyArr)
spacedArr = np.linspace(1,11,9,dtype=int)
print("The Spaces Array is",spacedArr)

dis = np.array([1,2,3,4,5,6])
print("The Spaces Array is",dis)

threedArray = np.array(
    [
        [[3,2,1],
         [6,5,4],
         [9,8,7]],
        [[5,3,8],
         [88,5,90],
         [44,332,22]]
    ]
)
sort = np.sort(threedArray)
# concat_arr = np.concatenate((sort,dis),axis=1)
# print("Concatenated array is",concat_arr)

arrange = np.reshape(sort,(3,3,2))
print(arrange)


np.linspace()