a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if(a>b) :
    if(b>c) :
        print(c , " is smallest.")
    else :
        print(b , "is smallest")
else :
    if(c>a) :
        print(a , " is smallest")
    else :
        print(c , " is smallest")