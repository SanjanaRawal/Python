try:
    num = int(input("Enter an even number: "))
    if num % 2 != 0:
        raise ValueError("The number isn't even.")
except ValueError as ve:
    print(ve)