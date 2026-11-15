#it is used very rarely but it is also a good and efficient way to use if statement. 
#Syntax to use this Statement.
# <var> = (false_value, true_value) [<condition]
age = int(input("Enter Age: "))
vote = ("yes", "no") [age < 18]
print("Can You Vote: ",vote)

#Here is a Second Example
salary = float(input("Enter Salary: "))
tax = salary*(0.2,0.1) [salary <= 50000]
print("Tax on Salary is", tax)