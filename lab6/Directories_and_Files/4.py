import os
path = "C://Users//User//Desktop//python_pp2//25_spring_pp2//lab6//Directories_and_Files//4.txt"
with open(path) as file_object:
    content = file_object.read()
    contents = content.split("\n")
    print(len(contents))