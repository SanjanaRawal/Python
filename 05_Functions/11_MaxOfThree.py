def max3(a,b,c) :
    max = a
    if max < b : max = b
    if max < c : max = c
    return max

print("Enter three numbers : ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

print("Maximum of all : " , max3(num1 , num2 , num3))
