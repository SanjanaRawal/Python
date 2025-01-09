dict1 = {"Name" : "ABC " , "Age" : 23 , "RollNo" : 45 , "Weight" : 56.9 , "Pass" : True}
print(dict1)
print(type(dict1))
#Slicing in dictionaries
print(dict1["Age"])
dict1["Name"]= "XYZ"
print(dict1)
print(dict1["Name"]) #will give error if no such key
print(dict1.get("Name")) #won't give error , will return none if no such key exist
print(dict1["Pass"])
print(type(dict1["Pass"]))