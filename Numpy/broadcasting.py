import numpy as np

# Broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions 
# So they match larger array's shape.
# The dimensions have the same size.
# Or
# One of the dimensions has the size of 1.

arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [10,11,12]])

arr2 = np.array([[0,0,0,0]])
arr3 = np.array([[1],[2],[3],[4]])

# For understanding the shapes of these 3 arrays
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

# Now we're broadcasting
print(arr2 * arr3)
print(arr3*arr1)

# Modifying arrays to get broadcasting with big numbers. 
arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(arr1.shape)
print(arr2.shape) # Expected output : (1,10) and (10,1) so that we can broadcast them together

# Broadcasting 
print(arr1*arr2)
