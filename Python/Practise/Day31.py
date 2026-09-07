#THIRD-PARTY MODULES
#NUMPY
#1-dimensional
import numpy as np
array=np.array([1,2,3,4])
print(array)
print(type(array))
print(array.size)
print(array.ndim)
#2-dimensional
array=np.array([[1,2,3,4],[5,6,7,8]])
print(array)
print(type(array))
print(array.size)
print(array.ndim)
#3-dimensional
array=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(array)
print(type(array))
print(array.size)
print(array.ndim)
#eg:1
array=np.array([[1,2,3,4],[5,6,7,8]])
print(array)
print(array.shape)
print()
print(array.reshape(4,2))
#converts to 1-d array
print(array.flatten())
#eg:2
array=np.zeros((2,3))
print(array)
array=np.ones((2,3))
print(array)
array=np.eye(2)
print(array)
array=np.full((2,3),7)
print(array)
#when diff data types passed it is converted into same data type
array=np.array([1,2,3,4.5])
print(array)
array=np.array([1,2,3,4.5,"raju"])
print(array)
array=np.array([1,2,3,4.5,True])
print(array)
array=np.arange(1,11,2)
print(array)
array=np.random.randint(1,100, (2,3))
print(array)
#returns float value
array=np.random.rand(1,100,2,3)
print(array)
array=np.array([1,2,3,4])
print(array+10)
print(array*2)
print(array**2)
print(array.__pow__(0.5))
print(np.sqrt(array))