l = [12,23,45,56,67,78,89,90]

def fx(num) :
    return num%2 == 0

print(l)
fnl = filter(fx , l)
print(fnl)
nl = list(fnl)
print(nl)