num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
print("Common multiples of " , num1 , " and " , num2 , " are : ")
for i in range(1 , 1001 , 1) :
    if i%num1==0 and i%num2==0 :
        print(i)