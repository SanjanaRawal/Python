lst = [123 , "abc" , 34.5 , True ]

#Using for loop
print("FIRST WAY")
for i in lst :
    print(i)

print("SECOND WAY")
for i in range(len(lst)) :
    print(i , " " , lst[i])

print("THIRD WAY")
[print(i) for i in lst]

#Using while loop
print("FOURTH WAY")
i=0
while i<len(lst) :
    print(i , " " , lst[i])
    i += 1

