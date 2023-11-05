'''
Ler um número inteiro e mostrar uma mensagem indicando se este número é
par ou ímpar, e se é positivo ou negativo.
'''

num = int(input('Digite o número'))

if num %2 == 0:
     print(f'O número {num} é par e ',end='')
else: 
     print(f'O número {num} é impar e ',end='')

if num > 0:
    print('positivo')
elif num < 0:
     print('negativo')
else:
     print('Zero')
     