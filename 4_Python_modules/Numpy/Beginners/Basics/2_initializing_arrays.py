import numpy as np

r_array = np.array([[1,2,3],
                    [1,2,3]])
sample = np.ones(shape=(1,1,3,4),dtype="float64")
print(f"Creating a ndarray with all zeros \n {np.zeros(5)}")

# shape = (size,duplication,row,column)

print(f"Creating a ndarray with all zeros \n {np.zeros(shape=(2,2,3,4))}")

print(f"creating arrays with all 1's \n{np.ones(shape=(1,2,2,2))}")

print(f"Filling the array with all 100's \n {np.full(shape=(2,2,2,3),fill_value=100.20,dtype='float64')}") 

print(f"generating array of random values \n{np.random.rand(2,3)}")

print(f"generating array of random values with existing sample \n{5*np.random.random_sample(sample.shape)}")

#random integers 
print(f"generating a array with random intergers \n {np.random.randint(low=-3,high=3,size=(2,3))}")

#identity
print(f"creating a identity matrix or array\n {np.identity(4)}")

#repeating an array 
print(f"Repeating a array \n{np.repeat(r_array,2,axis=0)}")