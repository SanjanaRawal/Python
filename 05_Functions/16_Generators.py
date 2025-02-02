def fx() :
    for i in range(10) :
        yield i

print(next(fx()))
print(next(fx()))
print("*******")
a = fx()
print(next(a))
print(next(a))
print(next(a))
print("*******")
for j in fx() :
    print(j)