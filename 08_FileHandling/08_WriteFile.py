print("Previous text in the file :\n", open("01").read())

f = open("01", mode ='w', buffering=10, encoding=None, errors=None, newline="\n")
print(f)
print(type(f))
f.write("I'm writing in the file which over writes the previous written text , and from now onwards this text will only be shown in the file.")
f.close()

print("New text in the file :\n", open("01").read())