def fib(n) :
    a = 0
    b = 1
    if n<0 :
        print("Incorrect number given as input.")
    if n==0 :
        print(" ")
    elif n==1 :
        print(a)
    else :
        print(a)
        print(b)

    for i in range(3 , n+1 , 1) :
        next = a + b
        print(next)
        a = b
        b = next

num = int(input("Enter number : "))
fib(num)