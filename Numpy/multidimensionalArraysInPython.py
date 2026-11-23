import numpy as np

#Here's an example of 0 dimensional Array
a0 = np.array('A')
print(a0.ndim) # Returns the no. of dimensions

#Here's an example of 1 dimensional Array
a1 = np.array(['A','B','c'])
print(a1.ndim)

#Here's an example of 2 dimensional Array
a2 = np.array([['A','B','c'],
               ['D','E','F'],
               ['G','H','I']])
print(a2.ndim)

#Here's an example of 3 dimensional Array
a3 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
               [['A','B','C'],['D','E','F'],['G','H','I']],
               [['A','B','C'],['D','E','F'],['G','H','I']]])
print(a3.ndim)
# We need a consistent no. of elements in each list to create a 2d or 3d array, if any one of the list in the a3 array have lower or higher no. of elements, there will be a value error

print(a0.shape) # This one returns the shape of the array
print(a1.shape)
print(a2.shape)
print(a3.shape) 

# We can access the array elements just like c++
print(a3[2][1][2])
print(a2[1][2])
print(a1[2])
print(a2)
print(a1)
print(a3)

#Using string concatination, I am writing few Words.
word = a3[0,0,1] + a3[0,1,1] + a3[0,0,0] + a3[0,0,2] + a3[0,2,1]
print(word)