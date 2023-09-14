'''
Escreva um programa que leia uma string e imprima quantas vezes cada
caractere aparece nessa string.  String: TTAAC
 Formato de saída:
 T: 2x
 A: 2x
 C: 1x
'''
str1 = input('Digite a string ')
count = ''
for i in str1:
   if i not in count:
     count += i
     print(f'{i}: {str1.count(i)}x')
