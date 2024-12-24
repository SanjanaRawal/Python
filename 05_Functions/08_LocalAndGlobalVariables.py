x = 13
y = 34
print("x outside function without any change = " , x)
print("y outside function without any change = " , y)
print()

def printnum() :
    x = 99
    print("x in function after change in value = " , x)
    global y
    y = 49
    print("y in function after declaring global = ", y)

printnum()
print()
print("x outside function after change in value in function = " , x)
print("y outside function after declaring it global = " , y)