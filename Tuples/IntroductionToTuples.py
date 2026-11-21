# Tuples -> A built in data type that lets us create immutable sequences of values.
# we can access a particular element threw index but cannot change it.

tuple = (23,34,44,55,45,56,6,7,78)

print(tuple) #Gives complete tuple
print(tuple[4]) # Gives value of a particular index

tup = (1) # It is not a tuple, it is an integer
tup1 = (1,) # It is a tuple, this is the correct way to define a tuple

# Slicing also works in tuple, similar to lists and strings
print(tuple[1:3])
print(tuple[-5:-2])
