import os
path = "C://Users//User//Desktop//python_pp2//25_spring_pp2//lab6//Directories_and_Files//A.txt"
if os.path.exists(path):
    print("File exist")
else:
    print("File does not exist")
if os.access(path,os.R_OK) and os.access(path,os.W_OK) and os.access(path,os.X_OK):
    print("File accessable")
else:
    print("File is not accessable")
os.remove(path)