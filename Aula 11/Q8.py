'''
Escreva um programa que leia duas strings. Verifique se a segunda ocorre
dentro da primeira e imprima a posição de início.  1a string: AABBEFAATT
 2a string: BE
 Resultado: BE encontrado na posição 3 de AABBEFAATT
'''

str1 = input('Digite uma string ')
str2 = input('Segunda string ')

if str1.find(str2) == -1:
    print('A segunda string não está contida na primeira')
else:
    print(f'{str2} encontrado na posição {str1.find(str2)} de {str1}')
