a = (123 , "abc" , "  " , 90.99 , False)
print(a)
print(type(a))
#Slicing in tuples
print("SLICING IN TUPLES".center(60,"*"))
print(a[:])
print(a[::])
print(a[::-1])
print(a[1:5:2])
print(a[2:4:3])
print(a[0:len(a):2])
print(a[len(a) : 2 : -1])
print(a[8:1:-2])
#Iterations in tuples
print("ITERATIONS IN TUPLES".center(60,"*"))
print("FIRST WAY")
for i in a :
    print(i)
print("SECOND WAY")
for i in range(len(a)) :
    print(a[i])
print("THIRD WAY")
[print(i) for i in a]
print("FORTH WAY")
i=0
while i<len(a) :
    print(i)
    i+=1
