def fact(num) :
    if num <= 1 : return 1 ;
    ans = num * fact(num-1)
    return ans

a = int(input("Enter number : "))
print("Factorial = " , fact(a))