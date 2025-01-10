print(open("01").read())

f = open("01", mode ='a')
if f :
    print("File opened successfully")

f.write("\nThis time I'm appending the text , which won't over write but just add this content after the text already in file")
f.close()

f = open("01")
print(f.read())