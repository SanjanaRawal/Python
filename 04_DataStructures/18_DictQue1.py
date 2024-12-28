import json

# Sample data
data = {"Name": "Naman", "Age": 16, "Marks": 92}

# Print the original data and its type
print(data)
print(type(data))

# Convert data into JSON format (string)
fd = json.dumps(data)
print(fd)
print(type(fd))

#Convert json string into dictionary
dc = json.loads(fd)
print(dc)
print(type(dc))

# Pretty print JSON data
fd = json.dumps(data, indent=4)
print(fd)
print(type(fd))

# Sort JSON keys and write to a file
with open("18_data.json", mode="w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
print("JSON data copied successfully")

#print data from json file
with open("18_data.json" , mode="r") as f :
    d = json.load(f)
    print(d)




