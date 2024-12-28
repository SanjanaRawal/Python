dict1 = {"Name" : "ABC " , "Age" : 23 , "RollNo" : 45 , "Weight" : 56.9 , "Pass" : True}
print(dict1.get("Name"))
print(dict1.items())
print(dict1.values())
print(dict1.keys())
dict1.pop("Name")
print(dict1)
dict1.popitem()
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

