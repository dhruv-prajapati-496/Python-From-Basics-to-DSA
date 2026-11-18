# Check Armstrong Number
n = int(input("Enter Number: "))
if(n<0):
    print("Not Armstrong")
else: 
    temp = n
    total = 0
    totalDigits = 0
    while(n!=0):
        totalDigits += 1
        n //= 10
    n = temp
    while(n!=0):
        digit = n%10
        total += digit**totalDigits
        n //= 10
    print("Armstrong" if(temp == total) else "Not Armstrong")