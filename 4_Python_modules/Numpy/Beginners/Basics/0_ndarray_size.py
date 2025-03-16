import numpy as np 

a= np.array([1,2,3])

b = np.array([[3.4,4.4,3.0],
               [9.0,4.5,11.2]], dtype="float64")

print(b)


#ndim will provvide the number of dimenions that a numpy array has 
print(a.ndim)
print(b.ndim)

#shape 
print(a.shape)
print(f"(rows, columns) -> {b.shape}")

#we can also specify the datatypes of the array
print(f"data type of a array is -> {b.dtype}")

print(f"Total number of elements in the array rows*columns {b.size}")

print(f"we can get the size of he item in the array ndarray.itemsize -> {b.itemsize}")

#total size of the elements in the array 
print(f"The size of all the elements in the array ndarray.size*ndarrray.itemsize -> {b.size * b.itemsize}")

# we can also use the nbytes for getting the size of the total size of all elments in the array
print(f"Total size of all the elements in the array are -> {b.nbytes}")