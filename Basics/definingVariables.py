#Defining Variables in Python
name = "Dhruv Prajapati"
age = 20
price = 399.00
print("My name is ",name,".","My age is ",age,".","I bought a cake worth ",price,".\n") 
print("I know it didn't work well, but now it'll work cause i've understood the logic of f strings in python. See\n");
print(f"My name is {name}. My age is {age}. I bought a cake worth {price:.2f}.\n")

# An f-string is a formatted string in Python.

# You simply:
# - Put f before the opening quotation mark.
# - Put variables inside curly braces {}.
# - Python automatically replaces those curly braces with their values. 
# What does {price:.2f} mean?
# - : starts the formatting instruction.
# - .2 means display two digits after the decimal point.
# - f means floating-point number.
#Another Method using sep="", you can also remove the automatic spaces using sep = ""
print("hello","Reader\n",sep=" ")
print("My name is ",name,"."," My age is ",age,"."," I bought a cake worth ",price,".\n", sep="") 
#Price didn't worked well so i am using format string to make it showing 2 digits after decimal.
print("My name is ",name,".", "My age is ",age,"."," I bought a cake worth ",format(price,".2f"),".\n", sep="")
