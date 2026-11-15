# Find Greatest of 3 Numbers in python
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
if(num1 >= num2 and num1 >= 3):
    print(num1,"is greatest")
elif(num2>=num1 and num2>=num3):
    print(num2,"is greatest")
elif(num3>=num1 and num3>=num2):
    print(num3,"is greatest")
else:
    print("No one is Greatest")
#2nd and efficient method

print(max(num1,max(num2,num3)),"is greatest")