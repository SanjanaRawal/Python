dict1 = {"Name" : "ABC " , "Age" : 23 , "RollNo" : 45 , "Weight" : 56.9 , "Pass" : True}
print(dict1.get("Name"))
print(dict1.items())
print(dict1.values())
print(dict1.keys())
dict1.pop("Name") #deletes key value pair as the key is mentioned
print(dict1)
dict1.popitem() #deletes last key value pair
print(dict1)
dict1.update({"Age": 45})
print(dict1)
dict1.clear()
print(dict1)
dict1.setdefault(2)
print(dict1)
d = {"H" : "Hello" , "W" : "World"}
dict1 = d.copy()
print(dict1)
d2 = {123 : "OneTwoThree"}
d.update(d2) # adds elements of d2 dictionary after the elements of d and modifies d
print(d)
del d["H"] #deleted key value pair with index as H
print(d)
del d2 #deletes d2 , now accessing d2 will five an error