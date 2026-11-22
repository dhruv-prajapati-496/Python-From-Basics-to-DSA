# A Class is a collection of two things : 1. Methods 2. data attributes
# Methods are functions that belongs to objects
# Creating Class
class student:
    def __init__(self,fullname):
        self.name = fullname

    def hello(self):
        print("hello",self.name)

# Creating Object
s1 = student("Dhruv")
s1.hello()