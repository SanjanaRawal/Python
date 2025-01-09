try :
    dividend = int(input("Enter dividend : "))
    divisor = int(input("Enter divisor : "))
    print("Quotient = " , dividend//divisor)
    print("Remainder = " , dividend%divisor)
except ZeroDivisionError :
    print("Anything divided by zero is infinite")
except ValueError :
    print("Invalid data type entered")
#finally is always executed , even if there's an error or function is returned
finally :
    print("Program ended guys")