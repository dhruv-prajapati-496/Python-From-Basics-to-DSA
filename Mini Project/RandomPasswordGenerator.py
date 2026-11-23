import random
import string

pass_len = int(input("Enter Password Length: "))

charValues = string.ascii_letters + string.digits + string.punctuation

Password = ""
for i in range (0,pass_len):
    Password += random.choice(charValues)
print("Password is:",Password)