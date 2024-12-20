year = int(input("Enter year : "))
if year%4==0 :
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("It's a leap year")
        else :
            print("It isn't a leap year")
    else :
        print("It's a leap year")
else :
    print("It isn't a leap year")