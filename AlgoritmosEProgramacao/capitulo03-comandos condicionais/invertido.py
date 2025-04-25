'''
Faça um algoritmo que leia um núemro de 4 dígitos e escreva-o invertido.
Por exemplo, se o número lido for 2548, o resultado será 8452.
'''

n = input()
resp = ''
for i in range(len(n)-1, -1, -1):
    resp+=n[i]
print(int(resp))