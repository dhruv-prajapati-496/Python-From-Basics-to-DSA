# Lists -> A Built in data type that stores set of values. 
# There is a very Big difference in arrays in cpp and lists in python, the differece is "You cannot store different data types in arrays but you can do it in Lists."
marks = [23,45.5,34,50,49.5]
print(marks[3]) # Gives access of a particular element in List
print(len(marks)) # returns length of List
student = ["Dhruv",135,"Jhansi",85.4] #Storing different data types in a list
#In python, Strings are immutable while Lists are mutable, Means in strings you can access a value in string but cannot change, In Lists you can access and change the value.
#List Slicing is very Similar to String Slicing
print(marks[3:])
print(student[-3:-1])