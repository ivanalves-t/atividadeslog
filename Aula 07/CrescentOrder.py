'''
Dados três valores distintos, fazer um programa que, após a leitura destes
dados, coloque-os em ordem crescente.
'''


'''
alternativo: menor = min(num1,num2,num3); maior = max(num1,num2,num3)
mid = (num1+num2+num3) - (maior+menor)

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

print(menor,mid,maior)
