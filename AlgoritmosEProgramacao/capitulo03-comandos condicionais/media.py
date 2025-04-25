'''
Faça um algoritmo que calcule a média de quatro números introduzidos pelo usuário
'''

n1, n2, n3, n4 = map(int, input().split())
media = sum(n1, n2, n3, n4)/4
print(media)