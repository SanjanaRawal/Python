class Parent :
    def __init__(self):
        print("Parent Class Called")

class Child1(Parent) :
    def __init__(self) :
        super().__init__()
        print("Child One Class Called")

class Child2(Parent) :
    def __init__(self) :
        super().__init__()
        print("Child Two Class Called")

Parent()
print("*"*20)
Child1()
print("*"*20)
Child2()
print("*"*20)