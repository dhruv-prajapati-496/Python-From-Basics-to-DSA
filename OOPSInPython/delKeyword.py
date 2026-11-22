# Del Keyword : Used to delete object properties or object itself
class student:
    def __init__(self,name):
        self.name = name

s1 = student("Dhruv")
print(s1.name)

del s1.name
#del s1  : This deletes the entire object
print(s1.name)