import numpy as np

'''
pattern = [[1,1,1,1,1],
           [1,0,0,0,1],
           [1,0,9,0,1],
           [1,0,0,0,1],
           [1,1,1,1,1]]'''

#creating the above pattern
pattern = np.ones(shape=(5,5))
pattern[1:-1,1:-1] = np.zeros((3,3))
pattern[2,2] = 9

print(pattern)