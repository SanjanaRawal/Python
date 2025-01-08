import datetime

print("Hello , Today we will calculate the age!!!!!!")
person_name = input("Enter person whose age is to be calculated : ")
birth_year = int(input("Enter birth year : "))
birth_month = int(input("Enter birth month in figures : "))
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
person_age = 0
if birth_month > current_month :
    person_age = current_year - birth_year - 1
else :
    person_age = current_year - birth_year
print(person_name.capitalize() , " is " , person_age , " years old." )