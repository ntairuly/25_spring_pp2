import os
path = "C://Users//User//Desktop//python_pp2//25_spring_pp2//lab1//"
if os.path.exists(path):
    print("File exist")
else:
    print("File does not exist")
if os.access(path,os.R_OK):
    print("File is readable")
else:
    print("File is not readable")
if os.access(path,os.W_OK):
    print("File is writable")
else:
    print("File is not writable")
if os.access(path,os.X_OK):
    print("File is executable")
else:
    print("File is not executable")