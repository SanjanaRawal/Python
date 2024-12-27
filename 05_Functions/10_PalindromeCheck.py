def ispalindrome(n) :
    rev = 0
    num = n
    while num!=0 :
        rem = num % 10
        num = num // 10
        rev = rev*10 + rem
    if rev == n :
        print("Palindrome number")
    else :
        print("Not a palindrome number")

a = int(input("Enter number to check for palindrome : "))
ispalindrome(a)