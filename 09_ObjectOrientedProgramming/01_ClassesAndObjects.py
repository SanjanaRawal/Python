class Student :
    name = "xyz"
    cls = 10
    gpa = 7.2
    def information(self):
        return f"{self.name} has scored {self.gpa} in {self.cls} standard"

a = Student()
print(a)
print(a.name , a.cls , a.gpa)
print(a.information())
a.name = "Hiya"
print(a.name , a.cls , a.gpa)
print(a.information())
a.gpa = 8.1
print(a.name , a.cls , a.gpa)
print(a.information())
a.cls = 8
print(a.name , a.cls , a.gpa)
print(a.information())

b = Student()
b. name = "Sarita"
b.cls = 12
b.gpa = 6.8
print(b.name , b.cls , b.gpa)
print(b.information())