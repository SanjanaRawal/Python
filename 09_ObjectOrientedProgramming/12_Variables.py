class Student :
    school = "CPS" #class variable common for all the objects
    def __init__(self , name , id ):
        #instance variable that varies object to object
        self.name = name
        self.id = id
    def show(self):
        print(f"{self.name} is in {self.school} with id {self.id}")

s1 = Student("Rani" , "cp43")
s1.show()