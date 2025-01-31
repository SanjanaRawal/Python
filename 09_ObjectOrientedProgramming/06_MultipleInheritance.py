class Parent1 :
    def __init__(self):
        print("Parent One Class Called")
        super().__init__()  #call Parent2 __init__ for MRO

class Parent2 :
    def __init__(self):
        print("Parent Two Class Called")

class Child(Parent1 , Parent2) :
    def __init__(self) :
        super().__init__()
        print("Child Class Called")

Parent1()
print("*"*20)
Parent2()
print("*"*20)
Child()
print("*"*20)