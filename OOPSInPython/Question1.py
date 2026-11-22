# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class student:
    def __init__(self,name,physics,chemistry,maths):
        self.name = name
        self.physics_marks = physics
        self.chemistry_marks = chemistry
        self.maths_marks = maths

    def average_marks(self):
        return (self.physics_marks + self.chemistry_marks + self.maths_marks) / 3

s1 = student("Dhruv",78,87,96)
print("Name:",s1.name)
print("Physics Marks:",s1.physics_marks)
print("Chemistry Marks:",s1.chemistry_marks)
print("Maths Marks:",s1.maths_marks)
print("Average Marks",s1.average_marks())