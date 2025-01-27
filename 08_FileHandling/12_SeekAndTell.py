f = open("12_text" , "r")
print("File opened successfully")
#reads first 5 characters
txt = f.read(5)
print(txt)
#cursor moved to 4th character
f.seek(4)
#tells at which character cursor is currently
print(f.tell())
#reads 5 characters from 4th character
txt = f.read(5)
print(txt)