# List Methods
list = [2,1,3]
print(list)

list.append(4) # adds one more element to the end
print(list)

list.sort() # sorts list in ascending order 
print(list) 

list.sort(reverse=True) # sorts list in descending order
print(list)

list.reverse() # reverse list
print(list)

list.insert(3,5) # syntax: list.insert(idx,element) | insert element at index
print(list) 

# In python, Strings can also be sorted according to the letter arrangement using sort method
fruits = ["Litchi", "Banana", "Apple","Grapes"]
fruits.sort()
print(fruits)

list.remove(5) # Removes First occurence of an element
print(list)

list.pop(3) # Syntax : list.pop(idx) | It removes an element from a particular index
print(list)

