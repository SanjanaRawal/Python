a = int(input("Enter number : "))
sum = 0
for i in range(1 , a , 2) :
    sum += i
print("Sum of first " , int(a/2) ,  " odd numbers : " , sum)