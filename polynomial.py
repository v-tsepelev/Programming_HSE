# This class is currently under construction.

import math

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.n = 0
        self.visual = ""
    def degree(self):
        self.n = len(coefficients)
        return int(self.n)
    def output(self):
        for i in range(self.n):
            self.visual = self.visual + str(coefficients[i]) + "t^" + str(i)
        return str(self.visual)

arr = [1,2,3]
obj = Polynomial(arr)
n = obj.degree
out = obj.output
print(n)
print(out)
        
