# Sum of Digits
n = int(input("Enter A Number: "))
total = 0
while(n!=0):
    total += n%10
    n//=10
print("Sum of Digits: ",total)