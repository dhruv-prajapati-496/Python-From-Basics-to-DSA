n = int(input("Enter A Number: "))
prime = True
if(n<=1):
    prime = False
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        prime = False
        break
print("Prime" if prime else "Not Prime")