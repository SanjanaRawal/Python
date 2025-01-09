i=1
while i<11 :
    print(i)
    i +=1
else :
    print("1st else executed")

i=1
while i<11 :
    print(i)
    i += 1
    if i==10 :
        break
else :
    print("2nd else executed")