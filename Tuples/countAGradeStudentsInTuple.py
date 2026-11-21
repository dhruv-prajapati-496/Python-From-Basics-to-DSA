# WAP to count the number of students with the "A" Grade in the following tuple
Grade = ("C","D","A","A","B","B","A")
print("The number of students with grade 'A is:",Grade.count("A"))

# Second Question is to store above values in a list and print them into sorted order
list1 = []
for i in range (len(Grade)):
    list1.append(Grade[i])
list1.sort()
print(list1)