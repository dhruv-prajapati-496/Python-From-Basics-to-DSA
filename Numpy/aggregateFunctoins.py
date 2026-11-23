import numpy as np

# Aggeregate Functions : summarize data and typically return a single value

arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(np.sum(arr1)) # Returns sum of all values
print(np.mean(arr1)) # Returns mean of all values
print(np.std(arr1)) # Returns Standard deviation of all values
print(np.var(arr1)) # Retuns variation of all values
print(np.min(arr1)) # Returns minimum value of all the values
print(np.max(arr1)) # Returns maximum value of all the values
print(np.argmin(arr1)) # Returns position of minimum value
print(np.argmax(arr1)) # Returns position of maximum value

# There are also more advanced aggregate functions available inside numpy
print(np.sum(arr1,axis=0)) # Returns sum of all columns
print(np.sum(arr1,axis=1)) # Returns sum of all rows