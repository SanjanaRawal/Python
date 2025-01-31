class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real_sum = self.real + other.real
        img_sum = self.img + other.img
        return ComplexNumber(real_sum, img_sum)

    def __str__(self):
        if self.img >= 0:
            return f"{self.real} + {self.img}i"
        else:
            return f"{self.real} - {abs(self.img)}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
print(f"Sum : {c1 + c2}")