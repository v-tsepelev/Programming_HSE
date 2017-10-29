# This is the program that solves quadratic equation a*x^2+b*x+c=0 with user defined coefficients.

import math
import cmath
print("Please input coefficients of quadratic equation a*x^2+b*x+c=0 below")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = b**2-4*a*c
if abs(D) <= 1e-10:
    x = -b/(2*a)
    print('There is one real root x = {0} with double multiplicity'.format(x))
elif D > 1e-10:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)(2*a)
    print('There are two real roots: x1 = {0} and x2 = {1}'.format(x1,x2))
elif D < -1e-10:
    c1 = (-b+cmath.sqrt(D))/(2*a)
    c2 = (-b-cmath.sqrt(D))/(2*a)
    print('There are two complex roots: c1 = {0} and c2 = {1}'.format(c1,c2))
