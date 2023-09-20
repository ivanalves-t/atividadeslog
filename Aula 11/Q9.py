'''
Escreva um programa que leia duas strings e gere uma terceira com os
caracteres comuns às duas strings lidas.  1a string: AAACTBF
 2a string: CBT
 Resultado: CBT
 A ordem dos caracteres da string gerada não é importante, mas deve
conter todas as letras comuns a ambas.
'''

str1 = input('Digite uma string ')
str2 = input('Segunda string ')
comp = ''

for i in str1:
    if i in str2 and i not in comp:
                comp += i

if comp == '':
    print('Caracteres não encontrados na primeira string')
else:
    print(str2)
