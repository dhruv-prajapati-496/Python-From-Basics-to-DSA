# WAP to check whether a list contains palindrome elements or not ?

list1 = []

n1 = int(input("Enter number of elements of list: "))
print("Enter Elements in List: ")
for i in range(0,n1):
    list1.append(input())

temp_list = list1.copy()
temp_list.reverse()
print("Palindrome" if (list1 == temp_list) else "Not Palindrome")