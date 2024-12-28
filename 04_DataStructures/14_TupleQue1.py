t1 = ( 17 , 2 , 39 , 2 , 2 , 8 , 0 )
t2 = (4 , 5 , 12 , 55)

#Find length of second tuple
print(len(t2))

#Merge both tuples
print(t1+t2)

#Access 3rd element in t1
print(t1[2]) #element index is one less as indexing starts from 0

#Count occurrence of 2 in t1
print(t1.count(2))

#Check for an element in t1
print(99 in t1)

#Index of 12 in t2
print(t2.index(12))

#Max , min in t1
max = t1[0]
min = t1[0]
for t in t1 :
    if t < max : max = t
    if t > min : min = t
print("Max in t1 = " , max)
print("Min in t1 = " , min)

