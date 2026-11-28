import pandas as pd

# Series : A pandas 1-dimensional labled array that can hold any data type, think of it like a single column in a spreadsheet.

data = ([100,102,105])

series = pd.Series(data) # Series is a constructor, not a function so 's' should be capital. 

print(series)   # dtype:int64 means the series contains 64 bit of integers, if we manipulate data then the type also change.
print(type(series)) 

d1 = ([1.1,2.1,3.1])
s1 = pd.Series(d1)
print(s1)
print(type(s1))

# We can also manipulate the indexes as list, dictionary, a numpy array etc. By default the indexes are : 0,1,2,3,4....and so on.
d2 = ("Apple","Banana","Pipeapple","Strawberry","Orange","Grapes","Papaya")
s2 = pd.Series(d2,index=["a","b","c","d","e","f","g"])
print(s2)

# If we want to return the value inside a series, we can use the labled index to access it.
print(s2.loc["a"])
print(s2.loc["e"])
print(s1.loc[2])

# We can also manipulate data in a series using loc operator
s2.loc["d"] = "Mango"
print(s2.loc["d"])

# We can also filter Objects using comparision operators
d3 = ([100,22,33,456,32,453,232,102,345,674,98])
s3 = pd.Series(d3)
print(s3[s3 > 100])

# If we create a series using dictionary then by default, the keys will become our index.
calories = {"Day 1":1700 , "Day 2": 2000, "Day 3": 1800}
s4 = pd.Series(calories)
print(s4)
print(s4.loc["Day 3"])
# Lets Change the value of day 2.
s4.loc["Day 2"] += 500
print(s4.loc["Day 2"])