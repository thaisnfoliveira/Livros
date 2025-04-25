'''
Sabendo que a relação entre vértices, arestas e faces de um objeto geométrico é dada
pela fórmula:
vertices + faces = arestas + 2
calcule o número de vértices de um objeto geométrico genérico. A entrada será o 
número de faces e arestas (dadas por um número inteiro e positivo) e a saída será o
número de vértices.
'''

from math import sqrt

def equacao():
    a = int(input())
    b = int(input())
    c = int(input())
    delta = (b**2) -(4*a*c)
    x1 = (-b - sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a
    print(x1, x2)

equacao()