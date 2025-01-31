class Operations :
    def add(self ,a,b): #can be called only when object is created
        return a+b
    @staticmethod
    def sub(a, b): # can be called with or without creating object
        return a - b

# print(Operations.add(1,2 )) will give error
print(Operations.sub(3,8))
op = Operations()
print(op.add(1,2))
print(op.sub(5,8))