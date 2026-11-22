# Static Methods : Methods that don't use self parameters (work at class level)
class student:
    @staticmethod
    def college():
        print("Oist")

s1 = student()
s1.college()

# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
