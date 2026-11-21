# Dictionaries are used to store data values in in key:value pairs.
# They are mutable, unordered and don't allow duplicate keys
dict = {
    "key" : "value",
    "name" : "Dhruv",
    "CGPA" : 8.18,
    "marks" : [9,9,8,4],
    "subjects" : ("C++","Java","Python")
}
print(dict)
print(type(dict))

# to assign or add new
dict["CGPA"] = 8.2

# We can only access the value by using key in dictionary
# If we try to access a key which doesn't exists then python will give error

# Adding a new value in dictionaries
dict["Chess Rating"] = 1270
print(dict)