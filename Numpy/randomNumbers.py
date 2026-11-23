import numpy as np
# We can also generate random numbers using numpy

rng = np.random.default_rng() # It generates numbers ( integers and floating both) but not creates characters directly.

# Here's how to use it. 
print(rng.integers(1,20)) # Returns numbers from 1 to 20, 20 is exclusive
print(rng.integers(low= -20, high=365, size=5)) # Return an array of size 5 containg random elements from -20 to 365
print(rng.choice(list('abcdefghij'), size=5)) # Return an array of size 5 which contains the values "abcdefghij"

# if we want a 2D array then we can set dimensions like this:
print(rng.integers(low= -20, high=365, size=(5,3))) 

# Setting seed 
rng1 = np.random.default_rng(seed=1)
print(rng1.integers(low= -20, high=365, size=5)) # You'll get the same random value again and again cause seed=1

# Operations on floating point numbers
print(np.random.uniform()) # Return a random value between 0 and 1, uniform means each value will get an equal chance of being selected.
print(np.random.uniform(low=-1,high=5)) # Selecting range for section
print(np.random.uniform(-10,100,size=9)) # to return an array of size 9


# To use shuffle method using numpy random command
rng2 = np.random.default_rng()

arr = np.array([1,2,3,4,5])
rng2.shuffle(arr)
print(arr)

# To select a random fruit from a set of fruits
fruits = np.array(["apple","banana","coconut","pineapple","grapes","orange"])
fruit = rng2.choice(fruits)
print(fruit)

fruits1 = rng2.choice(fruits,size=2)
print(fruits1)