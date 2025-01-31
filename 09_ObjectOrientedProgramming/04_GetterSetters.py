class Stud :
    def __init__(self , name):
        self.name = name
    def show_name(self):
        print(f"Name of student is {self.name}")
    @property
    def NAME(self):
        return self.name
    @NAME.setter
    def NAME(self , value) :
        self.name = value

s1 = Stud("asha")
print(s1.name)
s1.show_name()

s1.NAME = "priya"
print("Name set to : ")
s1.show_name()