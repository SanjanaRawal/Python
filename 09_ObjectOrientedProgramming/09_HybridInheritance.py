#contains more than one type of inheritance - single . multiple , multilevel 
class Parent :
    def __init__(self):
        print("Parent Class Called")
        super().__init__()

class Parent2 :
    def __init__(self):
        print("Parent Two Class Called")

class Child1(Parent) :
    def __init__(self) :
        super().__init__()
        print("Child One Class Called")

class GrandChild(Child1) :
    def __init__(self) :
        super().__init__()
        print("Grand Child of child one Class Called")

class Child2(Parent , Parent2) :
    def __init__(self) :
        super().__init__()
        print("Child Two Class Called")

Parent()
print("*"*20)
Parent2()
print("*"*20)
Child1()
print("*"*20)
GrandChild()
print("*"*20)
Child2()
print("*"*20)