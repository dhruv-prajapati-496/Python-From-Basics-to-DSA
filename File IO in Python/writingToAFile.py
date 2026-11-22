# There are two methods to write in a file
f = open("C:/Coding/Python Learning Journey/File IO in Python/demo.txt","w") # 'w' mode is used to overwrite the file
# f.write("I like to watch hollywood and anime movies and webSeries") | this overwrites the entire file

f1 = open("C:/Coding/Python Learning Journey/File IO in Python/demo.txt","a") # 'a' mode is used to add new data to the file
f1.write("I like to watch hollywood and anime movies and webSeries")
