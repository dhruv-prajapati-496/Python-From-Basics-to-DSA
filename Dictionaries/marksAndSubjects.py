# WAP to enter marks of three subjects from the user and store them in a dictionary. Start with an emptu dictionary and add one by one. use subject name as key and marks as value.
dict = {}
Physics = float(input("Enter Physics Marks: "))
dict.update({"Physics" : Physics})

Chemistry = float(input("Enter Chemistry Marks: "))
dict.update({"Chemistry" : Chemistry})

Maths = float(input("Enter Maths Marks: "))
dict.update({"Maths" : Maths})

print(dict)