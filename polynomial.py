# This class is currently under development.

class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.n = len(self.coefficients)
        self.visual = ""

    def degree(self):
        return int(self.n)        

    def __add__(self, other):
        if isinstance(other, Polynomial):
            new_coefficients = []
            for i in range(max(self.degree(), other.degree())):
                new_coefficients.append(self.coefficients[i] + other.coefficients[i])
            return Polynomial(new_coefficients)
        else:
            new_coefficients = self.coefficients
            new_coefficients[0] = self.coefficients[0] + int(other)
            return Polynomial(new_coefficients)            

    def __sub__(self, other):
        new_coefficients = []
        for i in range(max(self.degree(), other.degree())):
            new_coefficients.append(self.coefficients[i] - other.coefficients[i])
        return Polynomial(new_coefficients)
        

    def __mul__(self, other):
        new_coefficients = []
        for k in range(self.degree() + other.degree() - 1):
            x = []
            for i in range(self.degree()):
                for j in range(other.degree()):
                    if (i + j == k):
                        x.append(self.coefficients[i]*other.coefficients[j])
            new_coefficients.append(sum(x))
        return Polynomial(new_coefficients)

    def __mod__(self, number):
        new_coefficients = []
        for i in range(self.degree()):
            new_coefficients.append(self.coefficients[i] % int(number))
        return Polynomial(new_coefficients)

    def __str__(self):
        self.visual = str(self.coefficients[0])
        for i in range(1, self.n-1):
            self.visual = self.visual + "+" + str(self.coefficients[i]) + "t^" + str(i)
        self.visual = self.visual + "+" + str(self.coefficients[self.n-1]) + "t^" + str(self.n-1)
        return str(self.visual)

arr1 = [1,2,3,4,5]
obj1 = Polynomial(arr1)
arr2 = [6,7,8,9,10]
obj2 = Polynomial(arr2)
print(obj1.coefficients)
print(obj2.coefficients)
print(obj1+2)
print((obj1+2).coefficients)
print(obj2 + 3)
print((obj2 + 3).coefficients)
print(obj1 + obj2)
print((obj1 + obj2).coefficients)
        
