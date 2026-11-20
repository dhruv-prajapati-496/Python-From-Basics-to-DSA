# LCM of Two Numbers
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
x,y = a,b
while b != 0:
    a,b = b,a%b
gcd = a
lcm = (x*y)//gcd
print("LCM is:",lcm)