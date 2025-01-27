from functools import reduce

l = [2, 4, 5, 7, 3, 8]
print(l)

nl = []
for i in range(len(l) - 1):
    x = l[i]
    y = l[i + 1]
    nl.append(x * y)
print(nl)

#product of all elements in the list
mul = reduce(lambda a, b: a * b, l)
print(mul)

def sub(num1 , num2) :
    return num2-num1

diff = reduce(sub , l)
print(diff)