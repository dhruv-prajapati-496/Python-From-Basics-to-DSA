# A constructor is a special method in object-oriented programming (OOP) that runs automatically whenever a new object of a class is created. 
# Its main job is to initialize the object's attributes (set up its starting data) and prepare it for use.
class student:

    #Default Constructor
    def __init__(self):
        pass

    #Parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student to the database..")

s1 = student("Dhruv",96)
print(s1.name,s1.marks)

s2 = student("Devansh",100)
print(s2.name,s2.marks)