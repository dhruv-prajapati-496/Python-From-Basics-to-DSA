#Type Casting means changing the data type of a variable by ourselves.
a = 2
print("Type of a before typecasting",type(a)) #Type of a before typecasting <class 'int'>
a = float(a)
print("Type of a after typecasting",type(a)) #Type of a after typecasting <class 'float'>
#this is how we can change the data type of a variable. 
#we can also change the data type of strings using type casting but the string should contain that floating or integer value in which we want to convert it. 
b = "5.25"
b = float(b)
print(b+a)  #7.25
#if there was a name or another string containing letters or symbols, then it'll give a type error
#if b = "Dhruv" then b+a will be a type error.
#we can also convert a string into a float or an int
num = 34.45
num = str(num)
print("Type of Num: ",type(num)) #Type of Num:  <class 'str'>
#as you can see we've converted the data type of a floating value into a string. 