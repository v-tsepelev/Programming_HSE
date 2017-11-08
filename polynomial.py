# This class is currently under construction.

import math

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.n = 0
        self.visual = ""
    def degree(self):
        self.n = len(self.coefficients)
        return int(self.n)
    def output(self):
        self.visual = str(self.coefficients[0])
        for i in range(1,self.n-1):
            self.visual = self.visual + "+" + str(self.coefficients[i]) + "t^" + str(i)
        self.visual = self.visual + "+" + str(self.coefficients[self.n-1]) + "t^" + str(self.n-1)
        return str(self.visual)

arr = [1,2,3,4,5]
obj = Polynomial(arr)
n = obj.degree()
out = obj.output()
print(n)
print(out)
        
