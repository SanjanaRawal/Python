class Stud :
    name ="abc"
    school = "CPS"
    def show(self):
        return f"{self.name} is in school named {self.school}"

    @classmethod
    def new_school(cls , school):
        cls.school = school

s1 = Stud()
print(s1.show())
s1.name = "San"
print(s1.show())
s1.school = "APS"
print(s1.show())