import datetime

rn = datetime.datetime.now()
print(rn)

a = datetime.datetime(1999,9 , 15)
print(a)
print(a.strftime("%A")) #complete day name
print(a.strftime("%a")) #short day name
print(a.strftime("%B")) #Complete month name
print(a.strftime("%b")) #short month name
print(a.strftime("%m")) #month number
print(a.strftime("%Y")) #complete year
print(a.strftime("%y")) #last two digits of year
print(a.strftime("%p")) #am or pm
print(a.strftime("%M")) #minutes
print(a.strftime("%S")) #Seconds
print(a.strftime("%f")) #microseconds
print(a.strftime("%X")) #Time