'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo
usuário (incluindo espaços em branco), conte: quantos espaços em branco
existem na frase. quantas vezes aparecem as vogais a, e, i, o, u. 11. Escreva um programa que leia uma string e imprima quantas vezes
'''
str1 = input('Digite uma string ')
count_spacebar = 0
count_vogals = 0

vogals_attributes = {
'a','e','i','o','u'
}

for i in str1:
    if i in vogals_attributes:
        count_vogals += 1
    if i == ' ':
        count_spacebar += 1

print(f'Na frase "{str1}" apareceram {count_spacebar} barras de espaço e {count_vogals} vogais')
