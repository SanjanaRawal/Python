class Person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
        print("Constructor called , values assigned")
    def info(self):
        print(f"{self.name} is {self.age} years old. " )

a = Person("Shweta" , 23)
a.info()
b = Person("Rahul" , 45)
b.info()