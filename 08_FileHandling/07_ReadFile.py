f = open("01", mode ='r', buffering=10, encoding=None, errors=None, newline="\n")
if f :
    print("File opened successfully")
print(f)
print(type(f))
text = f.read()
print(text)
f.close()