import os
path = "C://Users//User//Desktop//python_pp2//25_spring_pp2//lab6//Directories_and_Files//4.txt"
l = ["Helper","for","4","th","exersise"]
with open(path,"w") as file_object:
    for i in l:
        file_object.write(i+"\n")