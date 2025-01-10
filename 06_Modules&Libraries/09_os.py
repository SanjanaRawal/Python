import os

if os.path.exists("09_directory_made") == False :
    os.mkdir("09_directory_made")

if not os.path.exists("09_directory_made/inside 1") :
    for i in range(0,10,1) :
        os.mkdir(f"09_directory_made/inside { i+1 }")

print(os.listdir("09_directory_made"))

for i in os.listdir("09_directory_made") :
    print(i)

for i in os.listdir("09_directory_made") :
    print(i)
    print(os.listdir(f"09_directory_made/{i}"))