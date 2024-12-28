data = {"M" : 81 , "B" : 32 , "S" : 99 , "L" : 24}

#Print all key value pairs individually
for i,j in data.items() :
    print(i , " " , j)

#Access value at B
print("Value at B = " , data["B"])

#Sort dictionary by values
sdv = sorted(data.values())
print("Sorted data by values : " , sdv)

#Sort dictionary by keys
sdk = sorted(data.keys())
print("Sorted data by keys : " , sdk)

#Multiply all values in dictionary
prod = 1
for i in data :
    prod = prod*data[i]
print("Multiplication of values : " , prod)

#Create a dictionary with keys as numbers and values as square of the number present in key
a = int(input("Enter length of dictionary : "))
dict1 = {}
for i in range(1,a+1,1) :
    dict1[i] = i**2
print("The required dictionay is as follows : ")
print(dict1)