str = "Indore is the cleanest city."
print(str)
#to find length of string
print("Length of string = " , len(str))
#to count any letter in string
print("Total Occurrence of letter t = " , str.count("t"))
#to count any letter in string in a given range
print("Total Occurrence of letter t in given range = " , str.count("t", 2 , 20))
#to convert str into uppercase
print("Upper case : " , str.upper())
#to convert str into lowercase
print("Lower case : " , str.lower())
#to make 1st letter capital
print("Capitalized : " , str.capitalize())
#to get index of a letter
print("1st occurrence of t : " , str.index("t"))
print("1st occurrence of t : " , str.find("t"))
#find returns -1 if not found , index returns error
#to get index of a letter over a range
print("1st occurrence of t in given range : " , str.index("t" , 11))
''''#to set a format
city = input("Enter your city : ")
result = "I live in {} "
print(result.format(city))'''
#to bring a string at between
print(str.center(100))
print(str.center(100 , "*"))
#Check for all characters as alphanumeric
print("All alphanumeric? " , str.isalnum())
#Check for all characters as alphabets
print("All alphabets? " , str.isalpha())
#Check for all characters as numeric
print("All numeric? " , str.isnumeric())
#Check for all characters as decimals
print("All decimals? " , str.isdecimal())
#Check for all characters as digits
print("All digits? " , str.isdigit())
#Check for all lower case
print("All lower cased? " , str.islower())
# Check for all upper case
print("All upper cased? " , str.isupper())
#Check for all spaces
print("All spaces? " , str.isspace())
#Check for starting letter as capital and rest as lower case
print("Title cased? " , str.istitle())
#To check how string ends
print("Ends with '.'? " , str.endswith("."))
print(str.endswith(str , 0 , 8))
#To check how string starts
print("Starts with 'I' ? " , str.startswith("I"))
#Lower to upper and vice versa
print("Swap cased : " , str.swapcase())
#To split the string
print("String after split : " , str.split(" "))
#Left justified string
print("Left justified as mentioned : \n" , str.ljust(10,))
#Right justified string
print("Right justified as mentioned : \n" , str.rjust(10))
#To replace a character/s
print("Replace the with d : " , str.replace("the" , "d"))
#To get last index of a letter
print("Last index of t is " , str.rindex("t"))
#To print 1st letter of all words as capital and rest all as lower - title case
print(str.title())

a = "!!!!Hellooooo!!!!!!!!!!!!!!!"
print(a.rstrip("!"))
print(a.replace("o","w"))
print(a.split("l "))
b="         "
print(b.isspace())
print(b.isprintable())
c = "\n"
print(c.isprintable())

s = "Hey my name is {}"
name = "Sanjana"
print(s.format(name))
s1 = "Hey my name is {name}"
print(s1)
s2 = f"Hey my name is {name}"
print(s2)
s3 = f"Hey my name is {{name}}"
print(s3)
print(f"My name is {name}")
print("My name is {name}")