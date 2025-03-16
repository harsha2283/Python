import numpy as np 


a = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])

var_3d_array = np.array([[[1,2],
                          [3,4]],
                         [[5,6],
                          [7,8]]],
                          )

print(a)

print(a.shape)

#accessing the elements in the array using indexes
print(f"Accessing element from the array [r,c] -> {a[1,6]}")

#getting a specific row 
print(f"A row from the array a -> {a[1,:]}")

#getting a column from the array 
print(f"collecting the data of the column in the array a -> {a[:,3]}")

#fetching elments in a certain range [start:stop:stepsize]
print(f"fetching elements from the array a -> {a[1,2:6:1]}")

print(f"fetching elements from the array a -> {a[1,2:-1   :1]}")

 #replacing the elements in the row's and columns of the array created by the numpy
#12 will be replaced with the 50
a[1,4]= 50
print(f"12 is replaced with 50 \n{a}")

#replacing the elements in the column 
a[:, 4] = 20
print(f"The values in the array after replacing a column in the array\n {a}")

#replacing the array column with the specific array values 
a[:,4] = [56, 67]
print(f"Replacing the array column with the list of data\n {a}")

#replacing the elements in the row 
a[0,:] = 0
print(f"The 1st row is repalced with the zeros\n {a}")

set_values = (1,2,3,4,5,6,7)
a[0,:] = set_values
print(f"The 1st row is repalced with the new set of values \n {a}")

#3d array
print(var_3d_array)

#indexing the 3d array
print(f"accessing a element in 3rd array {var_3d_array[1,0,1]}")

var_3d_array[0,0,:] = [11,12]
print(f"Replacing a row in the array \n {var_3d_array}")

var_3d_array[0,:,0] = [13,14]
print(f"Replacing a row in the ndarray \n{var_3d_array}")