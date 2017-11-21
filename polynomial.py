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
        return int(self.n-1)        

    def __add__(self, other):
        if isinstance(other, Polynomial):
            new_coefficients = []
            for i in range(max(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] + other.coefficients[i])
            return Polynomial(new_coefficients)
        else:
            #new_coefficients = self.coefficients
            #new_coefficients[0] = self.coefficients[0] + int(other)
            new_coefficients = []
            for i in range(self.degree() + 1):
                new_coefficients.append(self.coefficients[i])
            new_coefficients[0] = self.coefficients[0] + int(other)
            return Polynomial(new_coefficients)            

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            new_coefficients = []
            for i in range(max(self.degree() + 1, other.degree() + 1)):
                new_coefficients.append(self.coefficients[i] - other.coefficients[i])
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
        if isinstance(other, Polynomial):
            new_coefficients = []
            for k in range(self.degree() + other.degree() + 1):
                x = []
                for i in range(self.degree() + 1):
                    for j in range(other.degree() + 1):
                        if (i + j == k):
                            x.append(self.coefficients[i]*other.coefficients[j])
                new_coefficients.append(sum(x))
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
            self.visual = str(self.coefficients[0]) + "+" + str(self.coefficients[1]) + "t"
            return self.visual
        else:
            self.visual = str(self.coefficients[0]) + "+" + str(self.coefficients[1]) + "t"
            for i in range(2, self.degree()):
                self.visual = self.visual + "+" + str(self.coefficients[i]) + "t^" + str(i)
            self.visual = self.visual + "+" + str(self.coefficients[self.degree()]) + "t^" + str(self.degree())
            return self.visual

    def subst(self, x):
        result = 0
        for i in range(0, self.degree() + 1):
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
            
class RealPolynomial(Polynomial):
    
    def find_root(self, left_x, right_x, epsilon = 0.01):
        if self.degree() % 2 == 1:
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
        
    def locmin_value(self, left_x, right_x):
        x = self.der().find_root(left_x, right_x, epsilon = 0.01)
        if self.substder(x, 2) > 0:
            return x
        
    def locmax_value(self, left_x, right_x):
        x = self.der().find_root(left_x, right_x, epsilon = 0.01)
        if self.substder(x, 2) < 0:
            return x

arr1 = [1]
obj1 = Polynomial(arr1)
arr2 = [2,3]
obj2 = Polynomial(arr2)
arr3 = [4,5,6]
obj3 = Polynomial(arr3)
arr4 = [7,8,9,10]
obj4 = Polynomial(arr4)
print(obj1)
print(obj2)
print(obj3)
print(obj4)

