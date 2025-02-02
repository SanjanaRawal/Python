from functools import lru_cache
#lru = Least Recently Used cache

@lru_cache(maxsize=None)
def square(num) :
    print(f"Computing square of {num}.......")
    return num*num

print(square(5))
print(square(11))
print(square(62))
print(square(5))
print(square(9))
#for repeated numbers , the square is stored in cache and directly returned when function is called in a program and doesn't print the corresponding statement
print(square(11))
print(square(5))