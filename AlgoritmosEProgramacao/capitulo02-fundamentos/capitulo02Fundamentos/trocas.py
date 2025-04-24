'''
Faça um algoritmo que armazene dois números em duas variáveis e que troque os
valores das variáveis.
'''

def troca():
    a = int(input())
    b = int(input())
    c = b
    b = a
    a = c
    print(a, b)

troca()