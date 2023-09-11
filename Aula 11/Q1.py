'''
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
seu comprimento. Informe também se as duas strings possuem o mesmo
comprimento e são iguais ou diferentes no conteúdo.
'''

str1 = input('Digite aqui algo: ')
str2 = input('Digite aqui algo: ')

if len(str1) == len(str2):
    print(f'Ambas tem {len(str1)} caracteres')
else:
    print(f'A primeira string tem {len(str1)} caracteres, e a segunda string tem {len(str2)} caracteres')

if str1 == str2:
    print('Mesmo conteúdo')
else:
    print('Conteúdo diferente')
    