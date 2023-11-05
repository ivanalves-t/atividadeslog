"""
Crie um algoritmo que receba um número inteiro, conte o número total de dígitos e
mostre o resultado. Por exemplo, se o número é 2021 , então a saída deve ser 4. Obs: O número não deve ser convertido para nenhum outro tipo, logo, todas as
operações devem ser realizadas sobre o número inteiro
"""

num = abs(int(input('Digite o número aqui: ')))
algarisms = 0

while True:
    num/=10
    algarisms += 1
    if num < 1: break

if algarisms > 1 : print(f'{algarisms} algarismos')
else: print(f'1 algarismo')