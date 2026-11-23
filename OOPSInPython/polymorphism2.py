# How we can use polymorphism using classes and objects for our use: 
# We can redefine a predefined function using dunder functions 
# Operators and dunder functions : 
# a+b is used for addition                              a.__add__(b)
# a-b is used for subtraction                           a.__sub__(b)
# a*b is used for multiplication                        a.__mul____(b)
# a/b is used for division                              a.__truediv____(b)
# a%b is used for mod                                   a.__mod____(b)

class complex: 
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i + ",self.img,"j",sep="")

    def __add__(self,num2): # Using dunder function to assign add operator a new task to add complex numbers.
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)

    def __sub__(self,num2):
            newReal = self.real - num2.real
            newImg = self.img - num2.img
            return complex(newReal,newImg)

num1 = complex(1,3)
num2 = complex(5,7)
num1.showNumber()
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num3
num4.showNumber()
# There are many types of dunder functions exist in python. 