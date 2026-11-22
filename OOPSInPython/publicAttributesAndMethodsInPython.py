# Private(Like) Attributes and methods
# Conceptual Implementations in python. 
# Private attributes and methods are meant to be used only within the class and are not accessible from the outside of the class
# To make an attribute private, we add two underscores in the starting of it's name. ex: __Attribute_name
class Account:
    def __init__(self, account_no, account_pass):
        self.accNumber = account_no
        self.__accPass = account_pass

user1 = Account("0105CS241135",25265252452)

print(user1.accNumber)
print(user1.accPass) # Will only work when accPass is public

# Only class internal function can use private methods and attributes.