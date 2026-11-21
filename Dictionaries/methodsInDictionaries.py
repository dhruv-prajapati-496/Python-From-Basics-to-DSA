# Methods in Dictionaries
myDict = {
    "name" : "Dhruv",
    "CGPA" : 8.18,
    "marks" : {
        "TOC" : 4,
        "DBMS" : 9,
        "DA" : 9,
        "IWT" : 8,
    },
    "Chess Rating" : 1270
}

print(myDict.keys()) # Returns all the keys in Dictionary

# We can also print values in list and touple data types using typecasting
print(list(myDict))

print(len(myDict)) # Returns number of key values in dictionary

print(myDict.values()) # Returns all the values in dictionary

print(myDict.items()) # Returns all the (key,value) pairs as touples

print(myDict.get("Chess Rating")) #Returns the value by passing key

# Now there are two methods to return the value, 1. myDict.get("name"), 2. myDict["name"]
# The Difference between both is, the method myDict.get("value") will not give error while the second easy way can give you error. This is the necessity of both funcitons in python.

myDict.update({"city" : "Jhansi"})
print(myDict)