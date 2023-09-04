'''
Escreva um programa para calcular o fatorial de um número fornecido pelo
usuário.
'''

num = int(input('Digite aqui o número: '))

fat = 1
i = 1

while i <= num:
    fat *= i
    i += 1

print(f'O fatorial de {num}! é {fat}')
