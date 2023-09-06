num = int(input('Digite um número inteiro '))

if num > 0:
    print(f'{num} é positivo e ',end='')
elif num < 0:
    print(f'{num} é negativo e ',end='')

if num %2 == 0 and num != 0:
    print('é par')
elif num %2 != 0:
    print('é ímpar')
else:
    print('Zero é Nulo')
    