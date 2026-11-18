# Check Palindrome Number
n = int(input("Enter a Number: "))
temp = n
rev = 0
while(n!=0):
    rev = rev*10 + n%10
    n //= 10 # it is used for floor division, and n /= 10 is used for float division in python
print("Palindrome" if (rev == temp) else "Not Palindrome")