f = open("10_text","r")
while True :
    text_line = f.readline()
    print(text_line)
    if not text_line :
        break
f.close()