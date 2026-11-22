# Python can be used to perform operations on a file (Read and Write Data)
# Types of all files : 1. Text files (.docx, .txt, .log etc) 2. Binary Files (.mkv, .jpeg, .mp4, .mp3, .mov etc)
# We can manipulate both types of the files using python.

# To open a file we use f = open("file_name","mode") : where file name is the name of file or the path of file and mode is the operation that we want to perform on it.
# Mode can be -> r : read mode, w : write mode
f = open("C:\Coding\Python Learning Journey\File IO in Python\demo.txt","r") 

# To read data, we use : data = f.read()
data = f.read()
print(data)

#To close an open file, we use : f.close()
f.close()

# Again opening it for more operations
f1 = open("C:\Coding\Python Learning Journey\File IO in Python\demo.txt","r") 

# Methods of reading a line
# We can use readline() method to read only a line of the file.
line1 = f1.readline()
print(line1)

# We can also read only a particular characters of data by passing paramether to the read() method
data1 = f1.read(10)
print(data1)

# File pointer/cursor: Python tracks where you are reading/writing in a file; read() moves it to EOF (End of File), so later reads return "" unless you reset it with seek(0).
remaining_part_of_file = f1.read()
print(remaining_part_of_file)

# Seeking the file so cursor points to the starting of the file
f1.seek(0)
remaining_part_of_file = f1.read()
print(remaining_part_of_file)  