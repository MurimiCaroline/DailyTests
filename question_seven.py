import numpy as np

# a) Use numpy to define an array, the shape of it is (5,5) and all elements of it is 0.
arr_a = np.zeros((5,5))
print("Array a:\n", arr_a)

# b) Create a 3x3 matrix with values ranging from 0 to 8
arr_b = np.arange(9).reshape(3,3)
print("Array b:\n", arr_b)

# c) Find indices of non-zero elements from [1,2,0,0,4,0]
arr_c = np.array([1,2,0,0,4,0])
non_zero_indices = np.nonzero(arr_c)
print("Indices of non-zero elements in array c:", non_zero_indices)

# d) Create a 10x10 array with random values and find the minimum and maximum values
arr_d = np.random.rand(10,10)
min_val = np.min(arr_d)
max_val = np.max(arr_d)
print("Array d:\n", arr_d)
print("Minimum value in array d:", min_val)
print("Maximum value in array d:", max_val)

# e) Create a random vector of size 30 and find the mean value
arr_e = np.random.rand(30)
mean_val = np.mean(arr_e)
print("Array e:\n", arr_e)
print("Mean value of array e:", mean_val)
