a = {"Hiiiee" , "Hellooo" , "Waddakam" , "Namaste" , "Salaam"}
#add a value
a.add("WORLD")
print(a)
#remove specific value
a.remove("Namaste")
print(a)
#same as remove
a.discard("WORLD")
print(a)
#remove any random value
a.pop()
print(a)
#copy sets
b=a.copy()
print(b)

print("*"*100)

s1 = {1,2,3,4,5}
s2 = {6,7,8}
s3 = {1,2}
print("Three sets s1 , s2 , s3 are as follows : " , s1 , s2 , s3)

#to check elements of one set are present in other or not
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s3))

#To check for subset
print(s1.issubset(s3))
print(s1.issubset(s1))
print(s3.issubset(s1))

#to check for superset
print(s1.issuperset(s3))
print(s1.issuperset(s2))
print(s1.issuperset(s1))
print(s3.issuperset(s1))

#Union of two sets by update
s4 = {1,4,6,19}
s1.update(s4)
print(s1)

#To make the set empty
s1.clear()
print(s1)

#union of two sets
s1 = {1,2,3,4,5}
s2={2,3,6,7,8}
print(s1.union(s2))

#difference of two sets - gives unique values in set
print(s1.difference(s3))

#To get common values of two sets
print(s1.intersection(s2))

#Intersection update - takes intersection and returns set s1 = intersection
s1.intersection_update(s2)
print(s1)

#Symmetric difference - Eliminated common elements
print(s1.symmetric_difference(s2))

#Symmetric difference , then update current set with sym diff
s1.symmetric_difference_update(s2)
print(s1)




