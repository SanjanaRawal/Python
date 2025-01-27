f = open("13_text" , "w")
f.write("Hello this is file number thirteen")
f.close()

with open("13_text" , "r") as f :
    print(f.read())

f = open("13_text","w+")
f.write("Hello World")
f.seek(0)
print(f.read())
f.truncate(5)
f.seek(0)
print(f.read())
f.close()