'''
Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras
maiúsculas. Dica: lembre-se que ao informar o nome, o usuário pode digitar
letras maiúsculas ou minúsculas.
'''

str1 = input('Digite seu nome ')
u = str1.upper()

for i in range(len(str1)):
    print(u[-i-1])
    