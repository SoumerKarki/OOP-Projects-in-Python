class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,other):
        return Complex(self.r+other.r, self.i+other.i)

    def __sub__(self,other):
        return Complex(self.r-other.r, self.i-other.i)

    def __mul__(self,other):
        return Complex(self.r*other.r-self.i*other.i, self.r*other.i+self.i*other.r)

    def __truediv__(self,other):
        r = (self.r*other.r + self.i*other.i)/(other.r**2 + other.i**2)
        i = (other.r*self.i - self.r*other.i)/(other.r**2 + other.i**2)
        return Complex(r,i)

    def __abs__(self):
        return (self.r**2 + self.i**2)**(0.5)

    def __neg__(self):
        return Complex(-self.r, -self.i)

    def __eq__(self,other):
        return self.r == other.r and self.i == other.i

    def __ne__(self,other):
        return not self.__eq__(other)

    def display(self):
        q=(self.r,self.i)
        print(q[0],"+i(", q[1],")")

complex1 = Complex(5,8)

complex2 = Complex(6,3)

complex1.display()

complex2.display()

print(" Addition: ")


complex3 = complex1 + complex2

complex3.display()

print(" Subtraction: ")

complex3 = complex1 - complex2

complex3.display()

print(" Multiplication: ")

complex3 = complex1 * complex2

complex3.display()

print(" Division: ")

complex3 = complex1 / complex2

complex3.display()

print(" Modulus: ")

a = complex3.__abs__()

print(a)

t = complex1 != complex2

print(t)

complex1 = -complex1

complex1.display()







