'''
Escreva um programa para contar a quantidade de números pares entre dois
números quaisquer fornecidos pelo usuário
'''

num = float(input('Digite um número'))

contador = 0
i = 2
while i <= num:
    num -= 2
    contador += 1

print(contador)
