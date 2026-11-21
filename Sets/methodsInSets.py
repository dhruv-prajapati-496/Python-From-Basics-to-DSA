# Methods in sets
collection = {5,1,2,2,3,4,"Dhruv",1270}
print(collection)

collection.add("Jhansi") # Adds an element in the set
print(collection)

collection.remove(1270) # Removes an element in the set
print(collection)

#We can add strings and tuples in sets but cannot add list in a set because list is mutable and set stores only immutable elements.

print(collection.pop()) # removes a random value

collection.clear() # Empties the set
print(collection)

collection = {5,1,2,2,3,4,"Dhruv",1270} # Assigning the old values again for reuse


collection2 = {45,43,23,45,4}

collection3 = collection.union(collection2) # Combines both set values and returns new
print(collection3)

print(collection.intersection(collection2)) # Combines common set values and returns new