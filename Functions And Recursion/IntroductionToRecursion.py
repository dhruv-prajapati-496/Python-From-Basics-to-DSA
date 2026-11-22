# Recursion : When a function calls itself
def count_in_reverse(n):
    if(n==0):
        return
    print(n, end= " ")
    count_in_reverse(n-1)

n = int(input("Enter a Number: "))
count_in_reverse(n)