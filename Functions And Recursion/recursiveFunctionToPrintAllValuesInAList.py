# Recursive function to print all values in a list
def RecursiveFunctionToPrintAllValuesInAList(list1,idx):
    if(idx == len(list1)):
        return
    print(list1[idx],end=" ")
    RecursiveFunctionToPrintAllValuesInAList(list1,idx+1)
list1 = [1,2,3,4,5,6,7,8,9,0]
RecursiveFunctionToPrintAllValuesInAList(list1,0)