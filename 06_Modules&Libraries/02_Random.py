import random

num = random.random() #Random value greater than 0 and less than 1
print(num)

a = random.randint(1,100) #Random integer in between 0 and 1
print(a)

lst = ["a" , "b" , "c" , "d" , "e" , "f"]
ch = random.choice(lst) #randomly choose between elements of the list
print(ch)