import os
filename = input("Enter file you want to open : ")
if os.path.isfile(filename) :
    f = open(filename)
    print("File opened successfully")
    f.close()
else :
    print("File not found")
