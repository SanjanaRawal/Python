def mul10(num) :
    return num*10

print(mul10(23))

l = [43,54,65,76]
new_l = []
for i in l :
    new_l.append(mul10(i))
print(l)
print(new_l)

#Alternatively ,
l2 = [12,23,45,67]
new_l2 = map(mul10 , l2)
print(new_l2)
nl2 = list(new_l2)
print(nl2)