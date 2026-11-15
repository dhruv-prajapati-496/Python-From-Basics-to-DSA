#Type conversion is conversion of data type of a variable. It is automatically done by the interpreter of python. 
a = 50
b = 100.00
c = a+b
print("Type of A",type(a))
print("Type of C",type(c))
# as you can see the type of c is float whether the type of a is int but we can also change the data type inside the variable.
a = a+4.0
print("Type of A after adding a float value: ",type(a))
#as you can see, after adding a float value inside a, the data type of a has changed. we cannot change data type of strings or interger,floats by using adding or substraction of a string. 
# if a = "2"
# and b = 3 then if we create a variable c = a+b then it'll give a type error. 