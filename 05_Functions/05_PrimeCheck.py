def isprime(num) :
    count = 0
    i = 1
    while i<=num :
        if num%i == 0 :
            count +=1
        i += 1
    if count == 2 :
        return num , "is prime"
    else :
        return num , "isn't prime"

a = int(input("Enter number : "))
ans = isprime(a)
print(ans)
