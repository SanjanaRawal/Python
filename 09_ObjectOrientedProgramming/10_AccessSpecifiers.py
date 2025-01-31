class Student :
    def __init__(self):
        self.name = "Suman" #public by default
        self.__gpa = 8.4 #private
        self._cls = 11 #protected

a = Student()
print(a)
print(a.name)
# print(a.cls) won't work as protected variables / functions can be accessed by class and child class only
print(a._cls) #somehow can be accessed as
# print(a.gpa) won't work as pvt means can't be accessed outside class itself
print(a._Student__gpa) #Somehow can be accessed as