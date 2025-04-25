'''
Faça um algoritmo capaz de identificar se um número é igual a 1, 5 ou 10. Caso não seja
nenhum desses valores, retornar a mensagem "Valor inválido".
'''

n = int(input())
if n == 1 or n==5 or n ==10:
    print("Valor válido!")
else:
    print("Valor inválido!")