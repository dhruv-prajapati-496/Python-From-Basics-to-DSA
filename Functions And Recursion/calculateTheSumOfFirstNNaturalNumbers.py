# Calculating the sum of first N natural numbers
def sum_of_N_Natural_Numbers(n):
    if(n==0):
        return 0
    return n + sum_of_N_Natural_Numbers(n-1)
n = int(input("Enter a number: "))
print("Sum of",n,"Natural Numbers is: ",sum_of_N_Natural_Numbers(n))