# This class is currently under development.

class Polynomial:

    def __init__(self, coefficients):
        if isinstance(coefficients, list):
            self.coefficients = coefficients
        elif isinstance(coefficients, int):
            self.coefficients = []
            self.coefficients.append(coefficients)
        elif isinstance(coefficients, Polynomial):
            self.coefficients = coefficients.coefficients
        elif isinstance(coefficients, dict):
            self.coefficients = []
            powers = sorted(coefficients.keys())
            for i in powers:
                self.coefficients.append(coefficients[i])
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
            #new_coefficients = self.coefficients
            #new_coefficients[0] = self.coefficients[0] + int(other)
            new_coefficients = []
            for i in range(self.n):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] + int(other)
            return Polynomial(new_coefficients)            

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            new_coefficients = []
            for i in range(max(self.degree(), other.degree())):
                new_coefficients.append(self.coefficients[i] - other.coefficients[i])
            return Polynomial(new_coefficients)
        else:
            for i in range(self.n):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] - int(other)
            return Polynomial(new_coefficients)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_coefficients = []
            for k in range(self.degree() + other.degree() - 1):
                x = []
                for i in range(self.degree()):
                    for j in range(other.degree()):
                        if (i + j == k):
                            x.append(self.coefficients[i]*other.coefficients[j])
                new_coefficients.append(sum(x))
            return Polynomial(new_coefficients)
        else:
            new_coefficients = []
            for i in range(self.n):
                new_coefficients.append(other*self.coefficients[i])
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

    def subst(self, x):
        result = 0
        for i in range(0, self.n):
            result += self.coefficients[i]*(x**i)
        return result
    
    def der(self, d = 1):
        #while d != 1:
            #new_coefficients = []
            #for i in range(self.n-1):
                #new_coefficients.append(self.coefficients[i+1]*(i+1))
            #d -= 1
            #return der(Polynomial(new_coefficients), d)
        if d == 1:
            new_coefficients = []
            for i in range(self.n-1):
                new_coefficients.append(self.coefficients[i+1]*(i+1))
            return Polynomial(new_coefficients)
        elif d > self.n:
            return int(0)
        else:
            new_coefficients = []
            for i in range(self.n-1):
                new_coefficients.append(self.coefficients[i+1]*(i+1))
            return Polynomial(new_coefficients).der(d-1)
        
    def dersubst(self, x, d = 1):
        return self.der(d).subst(x)
            
class RealPolynomial(Polynomial):
    pass

arr1 = [1,2,3,4,5]
obj1 = Polynomial(arr1)
arr2 = {2:4,1:3}
obj2 = Polynomial(arr2)
print(obj1)
print(obj2)
print(obj2.coefficients)
