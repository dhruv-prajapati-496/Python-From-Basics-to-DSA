import numpy as np
# Filtering : Refers to the process of selecting elements from an array that match a given conditions

ages = np.array([[23,45,65,32,16,17,18,25],
                 [23,32,45,54,65,56,36,63]])

teenagers = ages[ages < 20] # Return the teenagers
print(teenagers)

adults = ages[(ages >=18) & (ages <65)] # Since, Numpy uses c style arrays, we cannot use 'and' or && as and operator
print(adults)

notAdults = ages[(ages < 18) | (ages > 65)]
print(notAdults)

evens = ages[ages%2 == 0]
print(evens)

adults_0 = np.where(ages > 17, ages, -1) # All the values which are less than 18 will be replaced with -1 and the shape of array will remain the same.
print(adults_0)