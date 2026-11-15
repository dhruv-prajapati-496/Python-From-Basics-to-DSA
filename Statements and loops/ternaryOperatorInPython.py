#This file shows how to use ternary operator in python
# To use Ternary operator, we've to use this syntax:  <var> = <val1> if (condition) else <val2>
#For Example
food = input("Food: ")
eat = "Yes" if (food == "cake") else "No"
print(eat)
#we can use this ternary operator to assign a value in a variable and we can also directly use it to print.
food2 = input("Food: ")
print("Sweet" if food == "cake" or food == "jalebi" else "Not Sweet")