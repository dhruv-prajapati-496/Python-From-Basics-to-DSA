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

