dict1 = {"Name" : "ABC " , "Age" : 23 , "RollNo" : 45 , "Weight" : 56.9 , "Pass" : True}

#print all key names one by one
for i in dict1 :
    print(i)

#print all values individually
#Method one
for i in dict1 :
    print(dict1[i])
#Method two
for i in dict1.values() :
    print(i)

#Print all key value pairs individually
#Method one
for i in dict1.items() :
    print(i)
#Method two
for i,j in dict1.items() :
    print(i, " : ", j)