# There are two types of attributes : 1. class attribute 2. Instance Attribute

class student:
    college_name = "OIST" # Only stores 1 time in a memory : class attribute (Cause in a college database, student's college name will be same, we don't need to store it multiple times)
    marks = 50 # Let's create two attributes of same name but different types

    #Parameterized constructor
    def __init__(self, name, marks):
        self.name = name  # It is an Instance attribute : this will occupy memory every time the object is created
        self.marks = marks # Object attribute precedence will be higher than class attribute.
        print("Adding new student to the database..")

s1 = student("Dhruv",96)
print(s1.name,s1.marks)

s2 = student("Devansh",100)
print(s2.name,s2.marks)

print(s2.college_name)
print(student.college_name) #This will be the same as s2.college_name. 