import os
path = "C://Users//User//Desktop//python_pp2//25_spring_pp2//lab1"
dir = os.listdir(path)
flag = input("1.Only directories \n2.Only files \n3.All directories and files\n")
if flag == "1" or flag == "3":
    print("Directories:")
    for i in dir:
        if os.path.isdir(path+"//"+i):
            print(i)
if flag == "2" or flag == "3":
    print("Files:")
    for i in dir:
        if os.path.isfile(path+"//"+i):
            print(i)