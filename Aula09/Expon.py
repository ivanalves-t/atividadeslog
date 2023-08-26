'''
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de
potência da linguagem ou o operador de exponenciação.
'''

num1 = int(input('Digite o valor da base '))
num2 = int(input('Digite o valor do expoente '))

resultado = 1

i = 0
while i < num2:
    resultado *= num1
    i += 1

print(resultado)
