'''
Escreva um programa para calcular o fatorial de um número fornecido pelo
usuário.
'''

fatorial = 1

num = int(input('Digite o número '))
bomba = num

if num >= 1 or num == 0:

    print(f'{bomba}! = ',end='')
    for num in range (num,0,-1):
        fatorial *= num
        if num == 1:
            print(f'{num} = ', end='')
        else:
            print(f'{num} X ', end='')
    print(fatorial)

else:
    print('NÃO EXISTE FATORIAL DE NÚMERO NEGATIVO')
