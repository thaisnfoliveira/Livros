'''
Faça um algoritmo que encontre as raízes da equação 2x^2 + 4x - 3.
'''
from math import sqrt

def equacao():
    a = 2
    b = 4
    c = -3
    delta = (b**2) -(4*a*c)
    x1 = (-b - sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a
    print(x1, x2)

equacao()