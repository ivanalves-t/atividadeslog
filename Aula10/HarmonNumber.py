'''
Em Matemática, o número harmônico designado por define-se como
sendo a soma da série harmónica:

Faça um programa que leia um valor n inteiro e positivo e apresente o valor
de .
'''

num = int(input('Type the number'))

if num > 0:
    h = 1
    resultado = 0
    for i in range(1,num):
        resultado += h/i
    print(f'O número harmonico de {num} é {resultado}')
else:
    print('ERRO, DIGITE UM VALOR POSITIVO')