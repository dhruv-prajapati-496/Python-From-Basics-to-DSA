#String is a data type that sotres a sequence of characters
#Concatenation in Strings: 
# "Hello" + "World" ------> "HelloWorld"
a = "Hello"
b = "World"
print(a+b)
# length of String : we can find length of strings using function len(str_Name)
print("Length of String a is",len(a))
# we use escape sequencing characters in python to use nextline, tab etc in writing a string.
# \n is used for nextline
# \t is used for tab
print("This is a string.\nIt is used for next line.\n\tIt is used for tab.")

#we can access a character of a string in python using indexing just like c++
#We can only access character but we cannot assign and manipulate a character in python
String1 = "Dhruv Prajapati"
print(String1[6])
# String1[5] = "@" is not allowed in python

#In python Slicing Means Parts of a string, slicing is a major concept of python to learn Machine Learning.
# str[starting_index:ending_index] ending index is not included.
print(String1[1:4])
print(String1[:7]) #works as String1[0:7]
print(String1[4:]) #works as String1[4:len(String1)]

#Python have an additional Indexing concept which other languages didn't have, and that is negative indexing
#String "Dhruv" has positive and negative indexing both, "D" is at index 0 and -1 and in the same way "v" is at index 4 and -5
print(String1[-3:-1])
print(String1[-11:10])
print(String1[3:-5])