def sq(l) :
    lst = []
    for i in range (1 , l+1 , 1) :
        lst.append(i*i)
    print(lst)

size = int(input("Enter size of list : "))
sq(size)
