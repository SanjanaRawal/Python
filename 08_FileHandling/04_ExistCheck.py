import os
check1 = os.path.isfile("Helloo")
print("Helloo exist? " , check1)
if check1 :
    f = open("Helloo" , mode = "r")
    print("File opened successfully")
    #operations
else :
    print("File doesn't exist.")

check2 = os.path.isfile("01")
print("01 exists? " , check2)
if check2 :
    f = open("01", mode ="r")
    print("File opened successfully")
    #operations
else :
    print("File doesn't exist.")
