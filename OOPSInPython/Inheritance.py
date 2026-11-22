# Inheritance : When properties of a base class are inherited by the derived class
class car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(car): # This is the syntax to inherit the properties of another class into a class
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
car2.start() # Although car2 is an object of toyotacar but it also have properties of car. 