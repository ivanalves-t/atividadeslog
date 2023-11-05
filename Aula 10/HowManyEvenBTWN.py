'''
Escreva um programa para contar a quantidade de números pares entre dois
números quaisquer fornecidos pelo usuário
'''

num1 = int(input('Digite o primeiro Número'))
num2 = int(input('Digite o segundo número'))
count = 0

if num1 < num2:
    for num1 in range(num1,num2+1):
        if num1%2 == 0:
            count += 1
    print(count)

elif num1 > num2:
    for num2 in range(num2,num1+1):
        if num1%2 == 0:
            count += 1
    print(count)

else:
    print('Ta de sacanagem?')
    