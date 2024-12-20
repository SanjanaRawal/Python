print("Enter length three sides of triangle : ")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if (a+b > c) or (b+c > a) or (a+c > b) :
    print("It is a triangle")
else :
    print("It isn't a triangle")