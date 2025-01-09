def calculate() :
    a = int(input("Enter 1st number : "))
    op = input("Enter choice of operation : ")
    b = int(input("Enter 2nd number : "))
    match op:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case _:
            print("SYNTAX ERROR")

calculate()