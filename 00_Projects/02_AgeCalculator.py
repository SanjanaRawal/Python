import datetime
from dateutil.relativedelta import relativedelta

print("Hello, Today we will calculate the age!!!!!!")
person_name = input("Enter the person whose age is to be calculated : ")
print("Please take care of the format :) ")
d = input("Enter DOB in format YYYY-MM-DD: ")

DOB = datetime.datetime.strptime(d, "%Y-%m-%d")
current = datetime.datetime.now()

person_age = relativedelta(current, DOB)

if DOB.month == current.month and DOB.day == current.day:
    print(f"Happy birthday, {person_name}! Today you're {person_age.years} years old.")
else:
    print(f"{person_name.capitalize()} is {person_age.years} years, {person_age.months} months and {person_age.days} days old.")
