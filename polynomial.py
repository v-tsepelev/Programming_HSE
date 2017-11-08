# This class is currently under development.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.n = 0
        self.visual = ""
    def degree(self):
        self.n = len(self.coefficients)
        return int(self.n)        
    def __add__(self, other):
        for i in range(max(self.degree(), other.degree())):
            self.coefficients[i] = self.coefficients[i] + other.coefficients[i]
        new_coefficients = self.coefficients
        return Polynomial(new_coefficients)
    def output(self):
        self.visual = str(self.coefficients[0])
        for i in range(1, self.n-1):
            self.visual = self.visual + "+" + str(self.coefficients[i]) + "t^" + str(i)
        self.visual = self.visual + "+" + str(self.coefficients[self.n-1]) + "t^" + str(self.n-1)
        return str(self.visual)

arr1 = [1,2,3,4,5]
obj1 = Polynomial(arr1)
arr2 = [6,7,8,9,10]
obj2 = Polynomial(arr2)
print((obj1+obj2).output())
print(obj1.output())
print(obj2.output())
        
