# Numpy is a python library which means numeric python. it is used in data science and AI/ML.
# normally we use lists in python like
list1 = [1,2,3]
# and for performing operations we can do this
list2 = list1*2
print(list2) 

# But you can see the list and duplicated and merged. Using numpy we can multiply 2 in each element in the list.
import numpy as np 
print(np.__version__)

array = np.array([1,2,3])
array2 = array*2
print(array2)                   # Numpy arrays are 10x faster than lists
print(type(array2))