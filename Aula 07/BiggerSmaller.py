'''
Ler três números inteiros e mostrar o maior e o menor deles.
'''

num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
num3 = int(input('Digite um número'))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

mid = (num1+num2+num3)-(maior+menor)

print(f'O menor é {menor}, e o maior é {maior}')
