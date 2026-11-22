# We should open a file using with syntax and then perform operations on it. this is the efficient way to write code.
with open("File IO in Python/demo.txt","r") as f:
    data = f.read()
    print(data)
with open("File IO in Python/demo.txt","r") as f1:
    data1 = f1.readline()
    print(data1)

# Rest part of Code