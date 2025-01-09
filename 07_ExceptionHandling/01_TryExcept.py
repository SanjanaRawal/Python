#execute the block of code return inside try
try :
    dividend = int(input("Enter dividend : "))
    divisor = int(input("Enter divisor : "))
    print("Quotient = " , dividend//divisor)
    print("Remainder = " , dividend%divisor)
#if code return inside try gives errors as mentioned , execute respective except block
except ZeroDivisionError :
    print("Anything divided by zero is infinite")
except ValueError :
    print("Invalid data type entered")
#else block executed when no exception is thrown
else :
    print("Code executed successfully")