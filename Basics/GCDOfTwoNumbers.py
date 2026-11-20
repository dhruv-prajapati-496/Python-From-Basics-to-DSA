# GCD of Two Numbers
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
while b!=0:
    a,b = b,a%b
print("GCD is:",a)
