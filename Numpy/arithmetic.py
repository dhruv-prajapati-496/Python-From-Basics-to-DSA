import numpy as np

# Scalar arithmetic

arr = np.array([1,2,3])
print(arr + 1) # Each value will be added with 1
print(arr - 3)
print(arr/2)
print(arr*3)
print(arr**4)

# Vectorized maths funciton

print(np.sqrt(arr)) # Square root built in function in numpy

arr1 = np.array([1.01,2.5,3.99])

print(np.round(arr1)) # Round to the nearest integer
print(np.floor(arr1)) # Round to the back integer
print(np.ceil(arr1)) # Round to the forward integer
print(np.pi) # Returns the value of pi

# Exercise
radius = np.array([2,7,22])
# To return the areas of circle if radious is stored in the array called radius
AreaOFCicles = (radius**2)*np.pi
print(AreaOFCicles)

# Element Wise arithmetic
# With element wise arithmetic, we can apply operations between single elements of each array
arr2 = np.array([1,2,3])
arr3 = np.array([4,5,6])

print(arr2 - arr3)
print(arr2 + arr3)
print(arr2 * arr3)
print(arr3 / arr2)
print(arr2 ** arr3)

# Comparision Operators : Using comparision operators, we can create boolean arrays, filter data and use element wise comparisions
scores = np.array([91,100,56,48,87,92])

print(scores == 100) # To return a boolean array.
print(scores >= 50)
print(scores < 50)

# We can also assign the elements using comparision operators
scores[scores > 70] = 99
print(scores)