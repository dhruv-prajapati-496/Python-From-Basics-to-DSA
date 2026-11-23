import numpy as np

# In slicing we use this syntax : array_name[start:end:step] 
# It is as same as string slicing

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print(arr[1:4]) # To print last three rows
print(arr[0:4:2]) # This is to give me every 2nd row
print(arr[1:]) # If we skip to write ending or starting index, it'll consider all the back elements if starting index is not given and all the forward elements if ending index is not given. Step size will be 1 by default
print(arr[::2]) # This will also give me every 2nd row
print(arr[::-1]) # Negative indexing will also work.

print(arr[:,0]) # for printing all rows but 1st column.
print(arr[:,3]) # for printing all rows but 4th column.
print(arr[:,1:3]) # for printing 2nd and 3rd column.
print(arr[:,::3]) # for printing all columns with step size 3
print(arr[0:2,0:2]) # This will give me 1st 2 columns of first two rows.
print(arr[0:2,2:]) # All columns except starting two of starting 2 rows.
print(arr[2:,0:2]) # Last two rows of first two columns.