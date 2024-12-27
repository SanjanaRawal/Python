num = int(input("Enter a number : "))
if 0<num<10 :
    print("One digit number")
elif 10<=num<100 :
    print("Two digit number")
elif 100<=num<1000 :
    print("Three digit number")
elif 1000<=num<10000 :
    print("Four digit number")
else :
    if num<0 :
        print("It's negative")
    else :
        print("It's grater than 10,000")