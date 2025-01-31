class Parent :
    def __init__(self):
        print("Parent Class Called")

class Child(Parent) :
    def __init__(self) :
        super().__init__()
        print("Child Class Called")

class GrandChild(Child) :
    def __init__(self) :
        super().__init__()
        print("Grand Child Class Called")

Parent()
print("*"*20)
Child()
print("*"*20)
GrandChild()
print("*"*20)