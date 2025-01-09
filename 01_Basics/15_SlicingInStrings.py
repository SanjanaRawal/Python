str = "I'm working on pycharm"
print(str[:])
print(str[::])
print(str[0:len(str):1])
print(str[0:len(str)-1:1])
print(str[2:7])
print(str[2:9:1])
print(str[::2])
print(str[5:8:2])
print(str[::5])
print(str[len(str) : 0 : -2])
print(str[:-4])
print(str[:len(str)-4])
print(str[-9:-2])
print(str[len(str)-9:len(str)-2])
#To reverse the string
print(str[::-1])

#iteration in strings - To get all letters of string one by one
for i in str :
    print(i)