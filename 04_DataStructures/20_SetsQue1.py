s = { 23 , 45 , 67 , 89 , 0 , 87 , 76 , 65 , 54 , 43 , 32 , 21 , 10}

#Find max and min value in set s
print("Maximum in set : " , max(s))
print("Minimum in set : " , min(s))

#Check for subset
s2 = { 23 , 0 , 43}
print("s = " , s)
print("s2 = " , s2)
print("s2 is subset of s? " , s2.issubset(s))

#Differene between 2 sets
print("Different elements in set s = " , s.difference(s2))


#Remove an item from set if present
# a = int(input("Enter number you want to remove from set : "))
a=87
if a in s  :
    s.remove(a)
    print("Element deleted")
else :
    print("Element not present in set.")
print("Set : " , s)

#Find common elements in three lists using sets
l1 = [1,2,3,4,5]
l2 = [2,3,6,7,8,9,0]
l3 = [0,3,1,7,5]
print(set(l1) & set(l2) & set(l3))


