# Module for work with polynomials.
# Author: Vladimir Tsepelev, tsepelev at openmailbox.org

import math

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
        self.count = 0
        self.visual = ""

    def degree(self):
        return int(self.n-1)        

    def __add__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for i in range(min(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] + other.coefficients[i])
            if self.degree() > other.degree():
                for i in range(other.degree() + 1, self.degree() + 1):
                    new_coefficients.append(self.coefficients[i])
            elif self.degree() < other.degree():
                for i in range(self.degree() + 1, other.degree() + 1):
                    new_coefficients.append(other.coefficients[i])
            if isinstance(other, QuadraticPolynomial) and len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return Polynomial(new_coefficients)
        else:
            new_coefficients = []
            for i in range(self.degree() + 1):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] + int(other)
            return Polynomial(new_coefficients)            

    def __sub__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for i in range(min(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] - other.coefficients[i])
            if self.degree() > other.degree():
                for i in range(other.degree() + 1, self.degree() + 1):
                    new_coefficients.append(self.coefficients[i])
            elif self.degree() < other.degree():
                for i in range(self.degree() + 1, other.degree() + 1):
                    new_coefficients.append(-other.coefficients[i])
            if isinstance(other, QuadraticPolynomial) and len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return Polynomial(new_coefficients)
        else:
            for i in range(self.degree() + 1):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] - int(other)
            return Polynomial(new_coefficients)

    def __neg__(self):
        new_coefficients = []
        for i in range(self.degree() + 1):
            new_coefficients.append(-self.coefficients[i])
        return Polynomial(new_coefficients)

    def __mul__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for k in range(self.degree() + other.degree() + 1):
                x = []
                for i in range(self.degree() + 1):
                    for j in range(other.degree() + 1):
                        if (i + j == k):
                            x.append(self.coefficients[i]*other.coefficients[j])
                new_coefficients.append(sum(x))
            if isinstance(other, QuadraticPolynomial) and len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return Polynomial(new_coefficients)
        else:
            new_coefficients = []
            for i in range(self.degree() + 1):
                new_coefficients.append(other*self.coefficients[i])
            return Polynomial(new_coefficients)

    def __mod__(self, number):
        new_coefficients = []
        for i in range(self.degree() + 1):
            new_coefficients.append(self.coefficients[i] % int(number))
        return Polynomial(new_coefficients)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        if isinstance(other, int):
            if self.degree() == 0:
                return self.coefficients[0] == other
            else:
                return False

    def __str__(self):
        if self.degree() == 0:
            return str(self.coefficients[0])
        elif self.degree() == 1:
            if self.coefficients[1] < 0:
                self.visual = str(self.coefficients[0]) + str(self.coefficients[1]) + "t"
            else:
                self.visual = str(self.coefficients[0]) + "+" + str(self.coefficients[1]) + "t"                
            return self.visual
        else:
            if self.coefficients[1] < 0:
                self.visual = str(self.coefficients[0]) + str(self.coefficients[1]) + "t"                
            else:
                self.visual = str(self.coefficients[0]) + "+" + str(self.coefficients[1]) + "t"                
            for i in range(2, self.degree()):
                if self.coefficients[i] < 0:
                    self.visual = self.visual + str(self.coefficients[i]) + "t^" + str(i)                    
                else:
                    self.visual = self.visual + "+" + str(self.coefficients[i]) + "t^" + str(i)                        
            if self.coefficients[self.degree()] < 0:
                self.visual = self.visual + str(self.coefficients[self.degree()]) + "t^" + str(self.degree())
            else:
                self.visual = self.visual + "+" + str(self.coefficients[self.degree()]) + "t^" + str(self.degree())                
            return self.visual

    def subst(self, x):
        result = 0
        for i in range(0, self.degree() + 1):
            result += self.coefficients[i]*(x**i)
        return result
    
    def der(self, d = 1):
        if d == 1:
            new_coefficients = []
            for i in range(self.degree()):
                new_coefficients.append(self.coefficients[i+1]*(i+1))
            return Polynomial(new_coefficients)
        elif d > self.degree():
            return int(0)
        elif d == self.degree():
            x = self.coefficients[self.degree()]
            for i in range(1, self.degree() + 1):
                x *= i
            return x
        else:
            new_coefficients = []
            for i in range(self.degree()):
                new_coefficients.append(self.coefficients[i+1]*(i+1))
            return Polynomial(new_coefficients).der(d-1)
        
    def dersubst(self, x, d = 1):
        return self.der(d).subst(x)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return (0, self.coefficients[0])
        else:
            if self.count < self.degree() + 1:
                self.count += 1
                return (self.count - 1, self.coefficients[self.count - 1])
            else:
                raise StopIteration
            
class RealPolynomial(Polynomial):
    
    def find_root(self, left_x = "none", right_x = "none", epsilon = 0.01):
        if isinstance(left_x, int) and isinstance(right_x, int) and self.subst(left_x)*self.subst(right_x) < 0:
            a = left_x
            b = right_x
            while abs(b - a) > epsilon:
                c = (a + b) / 2
                if self.subst(b)*self.subst(c) < 0:
                    a = c
                elif self.subst(a)*self.subst(c) < 0:
                    b = c
            root = (a + b) / 2
            return root
        else:
            a = -1000
            b = 1000
            while self.subst(a)*self.subst(b) >= 0:
                a *= 2
                b *= 2
            return self.find_root(a, b)
        
    def locmin_value(self, left_x, right_x):
        x = self.der().find_root(left_x, right_x, epsilon = 0.01)
        if self.substder(x, 2) > 0:
            return x
        
    def locmax_value(self, left_x, right_x):
        x = self.der().find_root(left_x, right_x, epsilon = 0.01)
        if self.substder(x, 2) < 0:
            return x
        
class QuadraticPolynomial(Polynomial):
    
    def __init__(self, coefficients):
        Polynomial.__init__(self, coefficients)
        if self.degree() > 2:
            raise Exception("Вы пытаетесь создать многочлен степени, большей чем 2")

    def __add__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for i in range(min(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] + other.coefficients[i])
            if self.degree() > other.degree():
                for i in range(other.degree() + 1, self.degree() + 1):
                    new_coefficients.append(self.coefficients[i])
            elif self.degree() < other.degree():
                for i in range(self.degree() + 1, other.degree() + 1):
                    new_coefficients.append(other.coefficients[i])
            if len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return QuadraticPolynomial(new_coefficients)
        else:
            new_coefficients = []
            for i in range(self.degree() + 1):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] + int(other)
            return QuadraticPolynomial(new_coefficients)            

    def __sub__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for i in range(min(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] - other.coefficients[i])
            if self.degree() > other.degree():
                for i in range(other.degree() + 1, self.degree() + 1):
                    new_coefficients.append(self.coefficients[i])
            elif self.degree() < other.degree():
                for i in range(self.degree() + 1, other.degree() + 1):
                    new_coefficients.append(-other.coefficients[i])
            if len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return QuadraticPolynomial(new_coefficients)
        else:
            for i in range(self.degree() + 1):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] - int(other)
            return QuadraticPolynomial(new_coefficients)

    def __mul__(self, other):
        if isinstance(other, Polynomial) or isinstance(other, QuadraticPolynomial):
            new_coefficients = []
            for k in range(self.degree() + other.degree() + 1):
                x = []
                for i in range(self.degree() + 1):
                    for j in range(other.degree() + 1):
                        if (i + j == k):
                            x.append(self.coefficients[i]*other.coefficients[j])
                new_coefficients.append(sum(x))
            if len(new_coefficients) > 3:
                raise DegreeIsTooBig(len(new_coefficients) - 1)
            else:
                return QuadraticPolynomial(new_coefficients)
        else:
            new_coefficients = []
            for i in range(self.degree() + 1):
                new_coefficients.append(other*self.coefficients[i])
            return QuadraticPolynomial(new_coefficients)

    def solve(self):
        if self.degree() == 0:
            return []
        elif self.degree() == 1:
            return [-self.coefficients[0]/self.coefficients[1]]
        else:
            a = self.coefficients[2]
            b = self.coefficients[1]
            c = self.coefficients[0]
            D = b**2-4*a*c
            if abs(D) <= 1e-10:
                x = -b/(2*a)
                return [x]
            elif D > 1e-10:
                x1 = (-b+D**0.5)/(2*a)
                x2 = (-b-D**0.5)(2*a)
                return [x1, x2]
            elif D < -1e-10:
                return []
        
class DegreeIsTooBig(Exception):
    
    def __init__(self, x, y = 2):
        self.x = x
        self.y = y

    def __str__(self):
        if isinstance(self.x, str):
            return self.x
        elif isinstance(self.x, int):
            error = "В результате операции получился многочлен степени {0}, максимально допустимая степень {1}".format(self.x, self.y)
            return error

