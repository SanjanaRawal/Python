def decor1(func) :
    def refunc(*args , **kwargs) :
        print("Decorator start , welcome to the program")
        func(*args , **kwargs)
        print("Decorator end , goodbye")
        print("*" * 70)
    return refunc

@decor1
def add(a,b) :
    print("Sum of " , a , " and ", b , " = " , a+b)

add(2,3)

def decor2(func) :
    def refunc() :
        print("Next piece of code starts")
        func()
        print("End")
        print("*" * 70)
    return refunc


def hello() :
    print("Hello dear")
decor2(hello)()

# @decor2
# def hello() :
#     print("Hello dear")
# hello()