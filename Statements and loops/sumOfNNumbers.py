# WAP to print sum of n numbers using while loop.
n = int(input("Enter a Positive Integer: "))
sum = 0
i = 0
if(n<0):
    print("Invalid Input")
else:
    while(i<=n):
        sum+=i
        i+=1
    print("Sum of first",n,"Numebers is:",sum)