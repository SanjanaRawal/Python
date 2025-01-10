f = open("01", mode ='w', buffering=10, encoding=None, errors=None, newline="\n")
if f :
    print("File opened successfully")
print(f)
print(type(f))
f.close()
